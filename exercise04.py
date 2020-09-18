from socket import *
from select import select


class WebServer:
    def __init__(self, host='0.0.0.0', port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.my_socket()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def my_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    def start(self):
        self.sock.listen(5)
        self.rlist.append(self.sock)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    connfd, addr = self.sock.accept()
                    print('Connect from', addr)
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    try:
                        self.handle(r)
                    except:
                        self.rlist.remove(r)
                        r.close()

    def handle(self, connfd):
        data = connfd.recv(1024).decode()
        info = data.split(' ')[1]
        if info == '/':
            filename = self.html + '/index.html'
        else:
            filename = self.html + info
        try:
            file = open(filename, 'rb')
        except:
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += 'Sorry'
            response = response.encode()
        else:
            fr = file.read()
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type:text/html\r\n'
            response += 'Content-Length:%d\r\n' % (len(fr))
            response += '\r\n'
            response = response.encode() + fr
            file.close()
        finally:
            connfd.send(response)


if __name__ == '__main__':
    httpd = WebServer(host='0.0.0.0',
                      port=8001,
                      html='./static')
    httpd.start()

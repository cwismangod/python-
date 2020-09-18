import sys
import time
from socket import *
from time import sleep

ADDR = (('127.0.0.1', 6666))


class FTPClient:
    def __init__(self, sock):
        self.sock = sock

    def do_list(self):
        self.sock.send(b'LIST')
        # 等待回复
        result = self.sock.recv(128).decode()
        if result == 'OK':
            # 接收文件列表
            files = self.sock.recv(1024 * 10)
            print(files.decode())
        else:
            print('文件库为空')

    def do_stor(self):
        file_name = input('想要上传的文件:')
        #判断本地文件是否存在
        try:
            fr = open(file_name,'rb')
        except:
            print('文件不存在')
            return
        # 提取文件名
        file = file_name.split('/')[-1]
        # 发送请求
        self.sock.send(('STOR ' + file).encode())
        result = self.sock.recv(128).decode()
        #分情况讨论
        if result == 'OK':
            while True:
                data = fr.read(1024 * 10)
                if not data:
                    break
                self.sock.send(data)
            # 表示文件已经发送结束
            sleep(0.1)
            self.sock.send(b'##')
            fr.close()
        else:
            print('文件已经存在')

    def do_retr(self):
        # 发送请求
        file_name = input('想要下载的文件:')
        msg = "RETR "+ file_name
        self.sock.send(msg.encode())
        #等待回复
        result = self.sock.recv(128).decode()
        if result == "OK":
            fw = open(file_name,'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()
        else:
            print('文件不存在')

    def do_exit(self):
        self.sock.send(b'EXIT')
        self.sock.close()
        sys.exit('谢谢使用')


def main():
    sock = socket()
    sock.connect(ADDR)

    ftp = FTPClient(sock)

    while True:
        print('\n========命令选项=========')
        print('       1.查看文件        ')
        print('       2.上传文件        ')
        print('       3.下载文件        ')
        print('       4.退出            ')
        print('========================\n')
        cmd = input('请输入命令:')
        if cmd == '1':
            ftp.do_list()
        elif cmd == '2':
            ftp.do_stor()
        elif cmd == '3':
            ftp.do_retr()
        elif cmd == '4':
            ftp.do_exit()

    sock.close()


main()

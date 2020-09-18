"""
进程基础实例2
含有参数的进程函数
"""

from multiprocessing import Process
from time import sleep

# 带有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working....")

# 创建进程
# p = Process(target=worker,args=(2,"Tom"))
p = Process(target=worker,
            args = (2,),
            kwargs={'name':'Levi'})

p.start()
p.join(3) # 最长等待3秒

print("================================")
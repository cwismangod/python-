"""
僵尸进程
"""

from multiprocessing import Process
from time import sleep
import os
from signal import *

# 带有参数的进程函数
def worker(sec,name):
    for i in range(2):
        sleep(sec)
        print(os.getpid(),"I'm %s"%name)


# 处理僵尸进程
signal(SIGCHLD,SIG_IGN)

# 创建进程
p = Process(target=worker,
            args = (2,),
            kwargs={'name':'Levi'})

p.start()

# p.join() # 防止僵尸产生

while True:
    pass
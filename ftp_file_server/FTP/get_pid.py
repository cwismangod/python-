"""
进程小函数——创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),"--",os.getpid())

def th3():
    sys.exit("退出进程")
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"--",os.getpid())

things = [th1,th2,th3]
jobs = [] # 存放进程对象
# 循环创建进程
for th in things:
    p = Process(target=th)
    jobs.append(p) # 进程对象存放起来
    p.start()

# 统一等待回收
for i in jobs:
    i.join()



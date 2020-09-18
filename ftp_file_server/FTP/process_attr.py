"""
进程对象属性说明
"""
from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

# 创建进程对象
p = Process(target=fun,name="tarena")

p.daemon = True # 必须在start前设置

p.start()

print("Name:",p.name) # 用于表示进程的作用
print("PID:",p.pid) # 进程编号
print("is alive:",p.is_alive())

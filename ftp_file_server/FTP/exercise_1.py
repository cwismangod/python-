"""
练习1 ： 大文件拆分
将一个 文件拆分为两个小文件

要求： 不清除文件类型 二进制  文本
      拆分的过程按照字节数平均分成两份
      上下两部分同时进行

提示： 两个进程同时拷贝
      os.path.getsize()
"""
from multiprocessing import Process
import os

filename = input("File:")
size = os.path.getsize(filename) # 获取文件大小

# 如果fr放在父进程中，那么父子进程使用fr的时候用的是
# 同一个文件偏移量，相互有影响
# fr = open(filename,'rb')

def top():
    # fr在各自子进程中打开那么他们各自用各自的文件偏移量
    fr = open(filename,'rb')
    fw = open("top.jpg",'wb')
    n = size // 2 # 一半大小
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpg", 'wb')
    fr.seek(size // 2)  # 偏移到一半大小
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

jobs = []
# 循环创建进程
for i in [bot,top]:
    p = Process(target=i)
    jobs.append(p)
    p.start()

[i.join() for i in jobs] # 回收进程

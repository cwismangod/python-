"""
创建进程基础示例1
1.将需要新进程执行的事件封装为函数
2.通过模块的Process类创建进程对象，关联函数
3.通过进程对象调用start启动进程
4.通过进程对象调用join回收进程资源
"""
import multiprocessing
from time import sleep

a = 1

# 进程的执行函数
def fun():
    print("开始运行一个进程")
    sleep(2)
    global a
    print("a = ",a)
    a = 10000      # 子进程中的变量a
    print("进程执行结束了")

# 实例化进程对象
p = multiprocessing.Process(target=fun)

# 启动进程 自动执行target绑定的函数，进程诞生
p.start()

print("执行另外一个事情")
sleep(3)
print("事情干完了")


# 阻塞等待进程结束后回收
p.join()

print("a :",a) # 父进程的a还是1
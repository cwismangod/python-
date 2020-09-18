"""
    学生信息管理系统
        MVC

    练习1：
        商品信息管理系统
            1. 创建商品模型类
                  商品名称
                  商品单价
                  商品编号
            2. 创建商品界面视图类
                   显示菜单
                   选择菜单
                   录入商品
            3. 创建商品逻辑控制器
                   添加商品(设置编号,存入列表)
    练习2：
            4. 显示商品信息
            5. 删除商品信息
"""


class StudentModel:
    """
        学生模型
            用于封装V与C传递的数据
    """

    def __init__(self, name="", sex="", score=0.0, age=0, sid=0):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        self.sid = sid  # 在系统中,数据的唯一标记


class StudentView:
    """
        学生界面视图
            负责处理界面逻辑(输入/输出)
    """

    def __init__(self):
        self.__controller = StudentController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加学生信息")
        print("2. 显示学生信息")
        print("3. 删除学生信息")
        print("4. 修改学生信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            # 先写方法调用语句,再alt + 回车,自动生成创建方法代码.
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.sex = input("请输入学生性别：")
        stu.score = int(input("请输入学生成绩："))
        stu.age = int(input("请输入学生年龄："))
        # 调用核心逻辑控制器C中的方法
        self.__controller.add_student(stu)

    def __display_students(self):
        for stu in self.__controller.list_students:
            print(f"{stu.name}的编号是{stu.sid},年龄是{stu.age},性别是{stu.sex},成绩是{stu.score}")

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")


class StudentController:
    """
        学生控制器
            对学生信息的核心处理逻辑(添加/删除/修改..)
    """

    def __init__(self):
        self.__list_students = []
        self.__start_id = 1000  # 如果有多个学生控制器,start_id会重复

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu_target):
        stu_target.sid = self.__start_id
        self.__start_id += 1

        self.__list_students.append(stu_target)

    # __start_id = 1000  # 如果有多个学生控制器,start_id不重复
    #
    # @classmethod
    # def set_student_id(cls,stu_target):
    #     stu_target.sid = cls.__start_id
    #     cls.__start_id += 1
    #
    # def __init__(self):
    #     self.__list_students = []
    #
    # def add_student(self, stu_target):
    #     StudentController.set_student_id(stu_target)
    #     self.__list_students.append(stu_target)
    def remove_student(self, sid):
        for i in range(len(self.__list_students)):
            if self.__list_students[i].sid == sid:
                del self.__list_students[i]
                return True  # 删除成功
        return False  # 删除失败


# 入口
view = StudentView()
view.main()

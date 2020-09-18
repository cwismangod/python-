'''
    学生管理系统
'''
class StudentModel:
    '''
        学生模型
            用于封装V与C传递的数据
    '''
    def __init__(self,name,sex,score,age,sid):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        self.sid = sid #在系统中,为数据的唯一标记

class StudentView:
    '''
        学生界面视图
            负责处理界面逻辑(输入输出)
    '''
    def __init__(self):
        self.__contruller = StudentController()
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
        item = input("请输入您的选项:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_student()

    def __input_student(self):

        stu = StudentModel
        stu.name = input("请输入学生姓名:")
        stu.sex = input("请输入学生性别:")
        stu.score = int(input("请输入学生成绩:"))
        stu.age = int(input("请输入学生年龄:"))

        self.__contruller.add_student(stu)

    def __display_student(self):
        pass

class StudentController:
    '''
        学生控制器
            对学生信息的核心处理逻辑(添加/删除/修改..)
    '''
    __start_id = 1000

    @classmethod
    def set_student_sid(cls, stu_target):
        stu_target.sid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__list_student = []

    def add_student(self,stu_target):
        StudentController.set_student_sid(stu_target)

        self.__list_student.append(stu_target)



#入口
view = StudentView()
view.main()






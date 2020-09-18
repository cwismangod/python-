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
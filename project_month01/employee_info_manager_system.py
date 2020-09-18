'''
    完成员工管理系统
        添加员工
        显示员工
        删除员工
        修改员工
'''
class EmployeeModle:
    def __init__(self,name = "", gender = "",age = 0,eid = 0):
        self.name = name
        self.gender = gender
        self.age = age
        self.eid = eid

    def __str__(self):
        return f"{self.name}的员工编号为{self.eid},性别为{self.gender},年龄是{self.age}"


    def __eq__(self, other):
        return self.eid == other.eid


class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()



    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


    def __display_menu(self):
        print("1. 添加员工信息")
        print("2. 显示员工信息")
        print("3. 删除员工信息")
        print("4. 修改员工信息")

    def __select_menu(self):
        item = int(input("请输入选项:"))
        if item == 1:
            self.__input_employee()
        elif item == 2:
            self.__display_employee()
        elif item == 3:
            self.__del_employee()
        elif item == 4:
            self.__change_employee()

    def __input_employee(self):
        emp = EmployeeModle()
        emp.name = input("请输入员工名字:")
        emp.gender = input("请输入员工性别:")
        emp.age = input("请输入员工年龄:")

        self.__controller.add_employee(emp)

    def __display_employee(self):
        for emp in self.__controller.list_employee:
            print(emp)
            # print(f"{emp.name}的员工编号为{emp.eid},性别为{emp.gender},年龄是{emp.age}")

    def __del_employee(self):
        eid = int(input("请输入想要删除员工信息的编号:"))
        if self.__controller.remove_list_commodity(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __change_employee(self):
        emp = EmployeeModle()
        emp.eid = int(input("请输入需要修改的员工编号:"))
        emp.name = input("请输入需要修改的员工名字:")
        emp.gender = input("请输入需要修改的员工性别:")
        emp.age = input("请输入需要修改的员工年龄:")
        if self.__controller.change_list_commodity(emp):
            print("修改成功")
        else:
            print("修改失败")





class EmployeeController:
    def __init__(self):
        self.__list_employee = []
        self.__start_eid = 1000


    @property
    def list_employee(self):
        return self.__list_employee

    def add_employee(self,emp_target):
        emp_target.eid = self.__start_eid
        self.__start_eid += 1

        self.__list_employee.append(emp_target)

    def remove_list_commodity(self, eid):

        emp = EmployeeModle(eid)
        if emp in self.__list_employee:
            self.__list_employee.remove(emp)
            return True
        return False
        # for i in range(len(self.__list_employee)):
        #     if eid == self.__list_employee[i].eid:
        #         del self.__list_employee[i]
        #         return True
        # return False


    def change_list_commodity(self,emp_target):
        for emp in self.__list_employee:
            if emp.eid == emp_target.eid:
                emp.name = emp_target.name
                emp.gender = emp_target.gender
                emp.age = emp_target.age
                return True
        return False





view = EmployeeView()
view.main()

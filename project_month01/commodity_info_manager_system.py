'''
    练习:1 创建商品模型类
            商品名称
            商品单价
            商品编号
        2. 创建商品界面视图类
            显示菜单
            选择菜单
            录入商品
        3. 创建商品逻辑控制器
            添加商品(设置编号,存入列表)
'''


class CommodityModel:
    '''
        商品模型
    '''

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid


class CommodityView:
    '''
        商品界面视图
    '''

    def __init__(self):
        self.__controller = CommodityController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加商品信息")
        print("2. 显示商品信息")
        print("3. 删除商品信息")
        print("4. 修改商品信息")

    def __select_menu(self):
        item = int(input("请输入您的选项:"))
        if item == 1:
            self.__input_commodity()
        elif item == 2:
            self.__display_commodity()
        elif item == 3:
            self.__del_commodity()
        elif item == 4:
            self.__change_commodity()

    def __input_commodity(self):
        com = CommodityModel()
        com.name = input("请输入商品名称:")
        com.price = input("请输入商品单价:")

        self.__controller.add_commodity(com)

    def __display_commodity(self):
        for com in self.__controller.list_commodity:
            print(f"{com.name}的商品编号为{com.cid},商品单价为{com.price}")

    def __del_commodity(self):
        cid = int(input("请输入想要删除商品信息的编号:"))
        if self.__controller.remove_list_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __change_commodity(self):
        com = CommodityModel()
        com.cid = int(input("请输入需要修改的商品编号:"))
        com.name = input("请输入修改的商品名称:")
        com.price = int(input("请输入修改的商品单价:"))
        if self.__controller.update_commodity(com):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    """
        商品控制器
            对商品信息的核心处理逻辑(添加/删除/修改..)
    """

    def __init__(self):
        self.__list_commodity = []
        self.__start_cid = 1000

    @property
    def list_commodity(self):
        return self.__list_commodity

    def add_commodity(self, com_target):
        com_target.cid = self.__start_cid
        self.__start_cid += 1

        self.__list_commodity.append(com_target)

    def remove_list_commodity(self, cid):
        for i in range(len(self.__list_commodity)):
            if self.__list_commodity[i].cid == cid:
                del self.__list_commodity[i]
                return True
        return False

    def update_commodity(self, com_target):
        for com in self.__list_commodity:
            if com.cid == com_target.cid:
                com.name = com_target.name
                com.price = com_target.price
                return True
        return False


# 入口
view = CommodityView()
view.main()

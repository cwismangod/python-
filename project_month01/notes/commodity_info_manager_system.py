"""
    商品信息管理系统
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    """
        商品界面视图
            负责处理界面逻辑(输入/输出)
    """

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
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))

        self.__controller.add_commodity(commodity)

    def __display_commoditys(self):
        pass


class CommodityController:
    """
        商品控制器
            对商品信息的核心处理逻辑(添加/删除/修改..)
    """

    def __init__(self):
        self.__list_commoditys = []
        self.__start_id = 1000

    def add_commodity(self, commodity_target):
        commodity_target.cid = self.__start_id
        self.__start_id += 1
        self.__list_commoditys.append(commodity_target)


# 入口
view = CommodityView()
view.main()

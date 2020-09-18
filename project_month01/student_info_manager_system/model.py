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
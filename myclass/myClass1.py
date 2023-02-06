class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student('eric', 20)
stu2 = Student('jack', 30)
print(stu1.name, stu1.age)
print(stu2.name, stu2.age)
print('---为stu2动态绑定性别属性---')
stu2.gender = 'man'
print(stu2.name, stu2.age, stu2.gender)
# python动态类型语言属性
stu1 = 88
print(stu1)


def show():
    print('这是一个定义在类之外的函数')


# 动态绑定方法
stu2.show = show
stu2.show()

"""
个数可变的位置参数
1.定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
2.使用*定义个数可变的位置形参
3.结果为一个元组
"""


def fun1(*args):
    print(type(args))
    return args


"""
个数可变的关键字形参
1.定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的关键字形参
2.使用**定义个数可变的关键字形参
3.结果为一个字典
"""


def fun2(**args):
    print(type(args))
    print(args)


fun1(10, 20, "str")
fun2(name='eric', age=18)


# 个数可变的位置参数，只能是一个
# 下面的代码会报错
# def fun3(*agr,*ar):
#     pass


# 个数可变的关键字参数，只能是一个
# 下面的代码会报错
# def fun3(**agr,**ar):
#     pass


# 在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参
# 要求个数可变的位置形参需在个数可变的关键字形参之前
def fun4(*args, **arg):
    print(type(args))
    print(type(arg))
    pass


fun4(10, 20, "str", name='eric', age=18)


# 方法内的全局变量，必须调用了该方法，才能生效
def fun5(a, b):
    global age
    age = 18
    return a + b + age


print(fun5(1, 2))
print(age)

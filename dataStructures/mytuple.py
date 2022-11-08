"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
"""
mytuple = ("java", 'python', 'eric', 18, "java")
print(type(mytuple))
# 列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等
print(dir(mytuple))
print(mytuple)

print("----python中for遍历----")
for item in mytuple:
    print(item)

print("----python中range()遍历----")
for index in range(len(mytuple)):
    print(mytuple[index])

print("----python中enumerate遍历----")
for index, value in enumerate(mytuple):
    print("index is " + str(index), ", value is " + str(mytuple[index]))

print("----python中iter遍历----")
for item in iter(mytuple):
    print(item)

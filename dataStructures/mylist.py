"""
python中list的数据项不需要具有相同的类型,与java的list类型类似，也是有序的，可以通过下标访问
"""
list1 = ["python", 99, "java", "company", "learning", 99.01]

print("----python中for遍历----")

for item in list1:
    print(item)

print("----python中range() 函数遍历----")

for index in range(len(list1)):
    print(list1[index])

print("----python中enumerate遍历----")

for index, value in enumerate(list1):
    print("index is " + str(index), ", value is " + str(list1[index]))

print("----python中iter遍历----")

for item in iter(list1):
    print(item)


print(type(list1))

# 列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等
print(dir())
print(dir(list1))

del list1


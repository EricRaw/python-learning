"""
python中set的数据与java的set类型类似，也是无序，不可重复的集合
"""
set2 = {2, 3, 99.33, "java"}
print(type(set2))
print(dir(set2))

# 打印set的大小
print(len(set2))

# 增加元素
set2.add("python")

# 移除元素,元素不存在则报错
# set2.remove("spark")
# 移除元素,元素不存在,无操作
set2.discard("spark")
# 随机删除一个元素
print(set2.pop())

list1 = ["python", 99, "java", "company", "python", 99.01]
# 将list数据类型去重
set3=set(list1)
print(set3)

# 取两个set的交集
set4 = set2 & set3
set4 = set2.intersection(set3)
print("取两个set的交集 "+str(set4))

# 取两个set的并集
set4 = set2 | set3
set4 = set2.union(set3)
print("取两个set的并集 " + str(set4))

# 取两个set的差集
set4 = set2 ^ set3
set4 = set2.difference(set3)
print("取两个set的差集 " + str(set4))


print("----python中for遍历----")
for item in set2:
    print(item)

print("----python中iter遍历----")
for item in iter(set2):
    print(item)

print("----python中enumerate遍历----")
for item in enumerate(set2):
    print(item)

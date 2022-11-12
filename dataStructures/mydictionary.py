"""
python中的字典类型与java中的map类型类似，都是键值对形式的数据格式(无序)，
其中value都可以存任意类型的值，如字符串、数字、元组、列表等其他容器模型。
key必须不可变，可以是数字、字符串、或元组,列表就不行。
"""
list1 = ["java", "python", "eric", 18]
dictionary = {"name": "eric", "age": 18, 18: 99, "list1": list1}

print(type(dictionary))
# 列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等
print(dir(dictionary))

# 访问字典中的某个值
print(dictionary['age'])
print(dictionary.get('age'))
# 访问字典中的某个值,值不存在不会报错，且可以赋默认值
print(dictionary.get('age88', '默认值为18'))

# 访问字典中的某个值，如果值不存在则会报错
# print(dictionary['age1'])

# 更新字典的某个值,如果值不存在则新增
dictionary['age'] = 30
dictionary['age1'] = 35

print(dictionary['age'])
print(dictionary['age1'])

# 删除字典中的某个元素
del dictionary['age1']
# 删除字典中的某个元素,值不存在会报错
# del dictionary['age99']

# 清除字典的所有元素
# dictionary.clear()

print("遍历key的方法1")
for k in dictionary:
    print(k)

print("遍历key的方法2")
for key in dictionary.keys():
    print(key)

print("遍历value的方法1")
for k in dictionary:
    print(dictionary[k])

print("遍历value的方法2")
for key in dictionary.keys():
    print(dictionary[key])

print("遍历value的方法3")
for v in dictionary.values():
    print(v)

print("同时遍历key和value的方法1")
for key, value in dictionary.items():
    print("key is " + str(key), " value is " + str(value))

print("同时遍历key和value的方法2")
for (key, value) in dictionary.items():
    print("key is " + str(key), " value is " + str(value))

print("同时遍历key和value的方法3")
for kv in dictionary.items():
    print("key and value is " + str(kv))


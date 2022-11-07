"""
python 常用类型之字符串及常用方法
"""
s1 = "hello python!"
s2 = "中文"
print(s1)
print(type(s1))
s2=s1+s2
print(s2)
i1=1
i2=88
"""
str() 和 repr() 函数虽然都可以将数字转换成字符串，但它们之间是有区别的：
str() 用于将数据转换成适合人类阅读的字符串形式。
repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），适合在开发和调试阶段使用；如果没有等价的语法，则会发生 SyntaxError 异常。
"""
s3=s1+s2+str(i1)+repr(i2)
print(s3)
# 获取字符串长度
slen='1234567890'
print(slen.__len__())
print(len(slen))
# 和java一样字符串类型首位是0
print(slen[0])
print(slen[1])
# 列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等
print(dir())
print(dir(slen))

s5="python"
s6="python"
print(s5==s6)
print(s5.__eq__(s6))
# python 中没有null类型，只有NoneType对象
s6=None
print(type(s6))

# 字符串驻留机制和字符串比较
# 字符串驻留：仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串驻留池中。Python 支持字符串驻留机制，对于符合标识符规则的字符串（仅包含下划线（_）、字母和数字）会启用字符串驻留机制驻留机制。
ss1 = "acc_99"
ss2 = "acc_99"
print(ss1.__eq__(ss2))
print(ss1 == ss2)
print(id(ss1))
print(id(ss2))

ss3 = "aabb"
ss4 = "cc"
ss5=ss3+ss4
print(ss3+ss4 =="aabbcc")
# id函数打印对象在内存中的地址
print(id(ss3+ss4))
print(id(ss5))
print(ss5 == "aabbcc")



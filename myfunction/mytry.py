try:
    n1 = int(input("请输入一个被除数"))
    n2 = int(input("请输入一个除数"))
    result = n1 / n2
    print(result)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("只能输入数字")
except BaseException as e:
    print(e)
else:
    print(result)
finally:
    print("程序结束")

class Student:
    native_place = '广东省'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def info(self):
        print('student name is ', self.name, ' age is', self.age)

    # 类方法
    @classmethod
    def cm(cls):
        print('this is 类方法')

    # 静态方法
    @staticmethod
    def sm():
        print('this is 静态方法')


print(Student.native_place)
Student.sm()
Student.cm()
student = Student('eric', 18)
print(student.name)
print(student.age)
print(student.native_place)
Student.native_place = '广州市'
print(student.native_place)
student.info()
student.cm()
student.sm()
print(type(Student))
print(type(student))
print(hash(Student))
print(hash(student))

class Person(object):  # 所有类默认继承 object，可省略
    def __init__(self, name):
        self._name = name  # 约定私有变量，外边可以使用
        self.__name = name  # 语法层面私有变量，外边无法使用

    @staticmethod
    def do():
        print("do sth")

    def say_hi(self):
        print(f"hello, i\"m {self._name}")

    def name(self):
        print(self._name, self.__name)

    @property
    def age(self): return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    __age = 18
    __test__ = {"content": "test"}  # 添加后缀 __ 取消私有

class Student(Person):  # 继承 Person
    def say_hi(self):
        """方法重写"""
        print(f"hello, i\"m {self._name}, i\"m a student")

john = Person("John")
john.say_hi()

tom = Student("Tom")
tom.say_hi()
tom.do()  # 调用父类方法

print(tom.__dict__)
print(tom._name)
# print(tom.__name)  # 报错
tom.name()  # Tom Tom
tom._name = "changed"
tom.__name = "changed"  # 外部可以以私有变量形式定义，但无法修改内部私有变量
tom.name()  # changed Tom
print(tom.__name)  # 外部变量
print(tom.__dict__)

def show(p: Person):
    p.say_hi()

show(john)
show(tom)

class Test:
    def say_hi(self):
        print("hello, i\"m test")

show(Test())

print(tom.age)
tom.age = 24
print(tom.age)
print(tom.__test__)

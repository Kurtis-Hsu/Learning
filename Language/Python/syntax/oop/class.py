class Person:
    print("define class Person")

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def say_hi(self):
        print("hello,", "i\"m", self.name)

    # static 方法，没有默认的 self 参数
    @staticmethod
    def info():
        print("I am a person")

tom = Person("tom")

print(type(tom))
print(isinstance(tom, object))  # 所有类都是 object 的子类
print(isinstance(tom, Person))

print(f"{tom.name} is {tom.age}")
print(tom.__dict__)  # 以字典形式打印一个对象

class Product:
    numbers = 0  # 类属性，相当于 Java 的 static 属性

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.numbers += 1

    # 类方法，默认第一个参数为当前类
    @classmethod
    def show_person_number(cls):
        print(f"当前有 {cls.numbers} 种商品")

pen = Product("pen", 10)
print(pen.__dict__)  # 没有 numbers
print(Product.numbers)
print(pen.numbers)

mouse = Product("mouse", 200)
print(Product.numbers)
print(pen.numbers)
print(mouse.numbers)

Person.say_hi(tom)
tom.say_hi()
Person.info()

Product.show_person_number()

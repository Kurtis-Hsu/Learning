class Person:
    def __init__(self, name):
        print("调用 __init__")
        self.name = name

    def __str__(self): return f"Person {self.name}"  # 相当于 Java 的 toString()

    def __add__(self, other): return f"{self.name} {other.name}"

tom = Person("Tom")
print(tom)
print(tom + Person("Jack"))

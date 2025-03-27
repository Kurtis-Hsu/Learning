def f():
    pass

def f(arg):
    pass

def f(arg: str):
    pass

def f(arg: str) -> None:
    print(f"function {arg}")

f("test")

def sum_2(a, b): return a + b

print(sum_2(1, 2))

def power(x, n=2): return x ** n  # 默认参数

print('power', power(2))
print('power', power(2, 3))

def info(name: str, age: int = 18, gender: str = "男"):
    print("我是%s，今年%d岁，是%s生" % (name, age, gender))

info("kurtis", 24, "男")
info("jack")
info("lily", gender="女")

# info("hallon", "女")

# 可变参数，接收一个元组
def dynamic(*args): print(type(args), args)

dynamic(1, 2, 3)
dynamic([1, 2])  # 将列表整个作为一个参数
dynamic(*[1, 2])  # 将列表元素作为可变参数

# 可变参数，接收一个字典（kw 表示 key-word，不强制）
def dynamic(**kwargs): print(type(kwargs), kwargs)

dynamic(a=1, b=2)
dynamic(**{"a": 1, "b": 2})

# 双星号参数必须是最后一个参数
def dynamic(x, **kwargs):
    print(x, type(kwargs), kwargs)

dynamic(a=1, b=2, x=3)

# 全局变量与局部变量
n1 = 10

def f():
    n1 = 30  # 创建了一个新的局部变量 n1，区别于全局变量 n1
    n2 = 20
    print("inner n", n1, n2)

f()
# print("outer", n1, n2)  # 无法使用 n2

print("outer n", n1)

x = 10  # 不可变数据类型
ls = [1, 2, 3, 4, 5]  # 可变数据类型

def f2():
    global x  # global 关键字声明使用全局变量
    x = 20
    ls[2] = 6  # 可变数据类型不需要使用 global 关键字
    print("inner x", x)
    print("inner ls", ls)

f2()
print("outer x", x)
print("outer ls", ls)

# lambda
fun = lambda a, b: a + b
print(type(fun), fun(1, 2))

ls = [1, 2, 3]
print(list(map(lambda i: i ** 3, ls)))

from package.pkg_lib import pkg_fun

pkg_fun()

from lib import fun
from sys import argv

fun(argv)

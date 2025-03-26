# 数据

# Python 变量不需要声明，变量的类型和值由可以随意改变
var = 1
print(type(var)) # type() 函数可以查看变量的类型
var = "hello world"
print(type(var))
var = 1.0
print(type(var))

v1, v2, v3 = 1, 2, 3

# print(v) # 未赋值的变量不可以直接使用，会报错

VAR = '123'  # Python 没有常量，一般约定变量名大写表示该变量不可修改

# 定义字符串
var = 'hello'
var = "hello" # 单引号和双引号没有区别

# 格式化字符串
var = "%d 年 %02d 月 %02d" % (2025, 3, 26)
print(var)
var = f"{2025} 年 {3:02d} 月 {26:02d}"
print(var)

# 正则表达式
var = r"^\d?$" # r 表示原始字符串，不会转义
print(var)

t, f = True, False # 布尔值

print("\n=== 列表 ===")

# 列表
var = [1, 2, 3, 4, 5]
var = list() # 这种方式只能创建空列表或者将其他类型转换为列表
var = [1, 'hello', 3.0, True, [1, 2, 3]] # 列表可以存放不同类型的数据

temp = ['123']
print("列表相加：", var + temp)
print("列表相乘：", var * 2)

print("列表比较：", [1, 2, 3] > [1, 3, 2]) # 比的是第一个元素，如果第一个元素相等，再比较第二个元素，以此类推

var = [1, 3, 2]
print("列表长度：%d，列表中的最小值：%d，列表中的最大值：%d" % (len(var), min(var), max(var))) # 列表中的元素必须是可比较的

for i in var: print("list element: ", i)

print(1 in var) # 判断元素是否在列表中

print("\n=== 集合 ===")

# 集合
var = {} # 这种方式创建的是字典
var = set() # 创建空集合
var = {1, 2, 3, 4, 5} # 集合是无序的，不重复的数据集合
var = set() # 这种方式只能创建空集合或者将其他类型转换为集合
var = {1, 'hello', 3.0, True, (1, 2, 3)} # 集合可以存放不同类型的数据

print("\n=== 元组 ===")

# 元组
var = (1, 2, 3, 4, 5) # 元组和列表类似，但是元组不可变
var = tuple() # 这种方式只能创建空元组或者将其他类型转换为元组
var = (1, 'hello', 3.0, True, [1, 2, 3]) # 元组可以存放不同类型的数据

var = (1) # 这种方式创建的是 int 类型
print(type(var))
var = (1,) # 只有一个元素的元组，需要在元素后面加逗号
print(type(var))

print("\n=== 枚举 ===")

# 枚举
var = enumerate(["man", "woman", "unknown"]) # enumerate() 函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
for i, v in var: print(i, v)

print("\n=== 字典 ===")

# 字典
var = {}
var = dict()
var = {
    "name": "张三",
    "age": 18,
    "gender": True,
    1: "123",
    True: "456", # 该键被解释器理解为与 1 相同，会覆盖上面的键
    2: "789",
}
print(var)
print(1 in var) # 判断键是否在字典中

for k, v in var.items(): print(k, v)
for k in var.keys(): print(k)
for v in var.values(): print(v)

print("\n=== 可遍历对象相关操作 ===")

var = [1, 2, 3, 4, 5]
print(var[0]) # 通过下标访问元素
print(var[-1]) # 负数下标表示从右往左
print(var[1:3]) # 切片操作，包含开始下标，不包含结束下标
print(var[:3]) # 从头开始
print(var[1:]) # 到末尾结束
print(var[::2]) # 步长为 2
print(var[::-1]) # 逆序

print("\n=== 类型转换 ===")

print("bin", int("100", 2))
print("oct", int("100", 8))
print("hex", int("100", 16))

print("int", int(True))
print("int", int(False))
print("int", int("123")) # 只有字符串表示的是数字时才能转换

print("float", float("123.456"))
print("float", float(True))
print("float", float(False))

print("str", str(123))
print("str", str(123.456))
print("str", str(True))
print("str", str(False))

print("bool", bool(0))
print("bool", bool(1))
print("bool", bool(123))
print("bool", bool(0.0))
print("bool", bool(0.1))
print("bool", bool(1.0))
print("bool", bool(""))
print("bool", bool("123"))

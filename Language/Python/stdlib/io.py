# Python 内置了 input 和 print 函数，用于输入和输出信息
# input 函数用于接收用户输入的信息，返回字符串类型
# print 函数用于输出信息到控制台

var = input("输入：")
print("输出：", var)

from pathlib import Path
Path("temp").mkdir(exist_ok=True) # 创建文件夹

# 输出到文件
# 打开文件，c 表示创建文件，w 表示写入文件，r 表示读取文件，a 表示追加内容
file = open("temp/temp.txt", "w", encoding="utf8")
file.write(f"first line {var}\n")
file.close() # 需要手动关闭文件

# 读取文件
file = open("temp/temp.txt", "r", encoding="utf8")
content = file.read() # 读取文件内容
print(content)
file.close()

# 追加内容
file = open("temp/temp.txt", "a", encoding="utf8")
file.write("second line\n")
file.close()
file = open("temp/temp.txt", "r", encoding="utf8")
content = file.read()
print(content)
file.close()

# 使用 with 语句自动关闭文件
with open("temp/temp.txt", "a", encoding="utf8") as file:
    file.write("third line\n")
with open("temp/temp.txt", "r", encoding="utf8") as file:
    content = file.read()
    print(content)

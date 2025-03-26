# 流程控制
var = True

# 选择语句
if var: print('do sth')
elif var: print('do another')  # Python 将 else if 合并为一个单词
else: print('do other')

# 循环语句
i = 0
while i < 5:
    print('Hello Python')
    i += 1

# 高斯求和
i = 0
result = 0
while i < 101:
    result += i
    i += 1
print(result)

for i in range(5): print('Hello Python')

# 高斯求和
result = 0
for i in range(101): result += i
print(result)

# break
for i in range(5):
    if i == 3: break
    print(f'break {i}')

# continue
for i in range(5):
    if i % 2 == 1: continue
    print(f'continue {i}')

# 搭配 else
i = 5
while i < 10:
    if i == 3: break
    i += 1
else:
    print("while else")

for i in range(10):
    if i == -1: break
else: print("for else")

# else 代码在循环正常结束后执行，若循环被 break 打断，不会执行 else 代码

# pass 指代空代码块
if True: pass

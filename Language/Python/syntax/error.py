print("name error:")
try:
    print("try")
except Exception as e:
    print("error:", e)
else:
    print("fun success")
finally:
    print("finally")

print("no error:")
try:
    print("do")
except Exception as e:
    print("error:", e)
else:
    print("print success")
finally:
    print("finally")

print("raise error:")
raise Exception("raise error")

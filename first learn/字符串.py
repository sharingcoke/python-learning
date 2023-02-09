name = """
someone
somebody
anyone
"""
# 单，双，三引号都可定义，可以定义多项
print(name)
name = '"hello"'
# 字符串中包含引号
print(name)
name = "\'world\'"
print(name)
# 字符串内包含引号，可以用转义字符


name_1="something"
name_2="help me"
print(name_2+name_1)

a=10
b=12.36
name="字符串拼接：%d以及%.1f"%(a,b)#
print(name)
print(f"1*2的结果:{a*b}")
#字符串格式化

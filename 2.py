from asyncio import PriorityQueue
from cgi import print_arguments
from unicodedata import decimal

a = open("/Users/xkg/Documents/test.txt", "a+")
print("http:\\\\www.baidu.com", file=a)
a.close()
print("55555\n44444")
print("55555\b444")
print("55555\r44444")
print('55555\t44444')
print("hello\"")
print("http:\\\\www.baidu.com")
print(r"55555\n44444")
print(chr(0b10000001100111111))
print(ord('徐'))
# 导入
import keyword

print(keyword.kwlist)
name = "科国"
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
print('值', name)
n = 10
print('类型', type(n))
print('八进制', 0o755)
print('二进制', 0b10101111)
print('十六进制', 0x789ad)
a = 1.1
a2 = 2.1
a3 = 2.2
print(a + a2)
print(a + a3)
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))
print('八进制', 0o755)
print('二进制', 0b10101111)
print('十六进制', 0x789ad)
print
print_arguments
print
#求随机数
import random
print(0)
print(random.randint(0, 10))
#求随机数
print("d")
import keyword
print(keyword.kwlist)
a=77
b=77.77
c=True
d=False
print(str(a),type(str(a)))
print(int(b),type(str(b)))
print(int(c),type(str(c)))
#浮点数
print(float(a),type(float(a)))
#字符串
print(str(a),type(str(a)))
#整数
print(int(b),type(int(b)))
#布尔值
print(int(c),type(int(c)))
#布尔值
print(int(d),type(int(d)))
#字符串
print(str(a),type(str(a)))
#浮点数
print(float(a),type(float(a)))
#字符串
print(str(a),type(str(a)))
#整数
print(int(b),type(int(b)))
#布尔值
print(int(c),type(int(c)))








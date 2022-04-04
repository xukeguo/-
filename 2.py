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

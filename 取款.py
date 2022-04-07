money=1010000
s=int(input("请输入取款金额："))
if s>money:
    print("余额不足")
else:
    print("取款成功")
    money=money-s
    print("我的钱包里有：",money)


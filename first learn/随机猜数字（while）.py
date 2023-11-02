import random

num = random.randint(1, 100)
i = 0
flag = True
while flag:
    guess = int(input("请输入你猜想的数字（1-100):"))
    if num == guess:
        print("猜对了")
        flag = False
    else:
        if num > guess:
            print("小了")
        else:
            print("大了")
    i += 1
print(f"你总共猜了{i}次")

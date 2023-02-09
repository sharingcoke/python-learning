import random

num = random.randint(1, 20)
guess = int(input("请输入你猜想的数字（1-20):"))
if num == guess:
    print("猜对了，太厉害了")
else:
    if guess > num:
        print("大了")
    else:
        print("小了")
    guess = int(input("请输入你猜想的数字（1-20):"))
    if num == guess:
        print("猜对了，太厉害了")
    else:
        if guess > num:
            print("大了")
        else:
            print("小了")
        guess = int(input("请输入你猜想的数字（1-20):"))
        if num == guess:
            print("猜对了，太厉害了")
        else:
            print("三次机会已用完，请重新开始")

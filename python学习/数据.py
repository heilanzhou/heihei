# s=0
# for i in range(100):
#     if i % 2:
#         s += i
#     else:
#         continue
# print(s)

# for i in range(100):
#     if i%2:
#         s +=i
#         if s>1000:
#             break
#     else:
#         continue
# print(s)

# ken =7
# while 1:
#     guess = int(input("请输入一个1-20的整数："))
#     if guess > ken:
#         print('数字太大')
#     elif guess < ken:
#         print('数字太小')
#     elif guess==ken:
#         print('恭喜你猜对了')
#         break

# import random
# a = 1
# b = 99
# key = random.randint(1, 100)
#函数功能：
#random.randint(参数1，参数2)；参数1、参数2必须是整数；函数返回参数1和参数2之间的任意整数

# while 1:
#     guess = int(input("请输入一个整数%d" % a + "到%d:" % b))
#     if guess<key and guess > a:
#         a = guess
#         print('请输入%d到' % a+"到%d" % b)
#     elif guess>key and guess<b:
#         b = guess
#         print('请输入%d' % a+"到%d" % b)
#     elif guess <= 1 or guess >= 100:
#         print("小伙子，别调皮，请重新输入")
#     elif guess == key:
#         print('真聪明，猜对了！')
#         break


# arr = [2, 9, 8, 0, 3, 4, 7]
# index = [0, 2, 4, 4, 5, 3, 5, 6, 1]
# QQ = ""
# for i in index:
#     QQ += str(arr[i]) #通过索引i查找对应arr列表中的数据，并拼接打印			  出来
# print("联系方式QQ："+QQ)


class People():

    def __init__(self,girl,live):
        self.girl = girl
        self.live = live
        print ("start!")

    def hand(self):
        h = "这是我对象的手:%s and %s"%(self.girl, self.live)
        return(h)

    def foot(self):
        f = "这是我对象的脚:%s and %s"%(self.girl, self.live)
        return(f)

if __name__ == "__main__":
    # 创建一类的实例，初始化：girl/live
    girlfriend = People('杨幂','娱乐')
    # 访问类的属性
    print (girlfriend.girl)
    print (girlfriend.live)
    print(girlfriend.foot())
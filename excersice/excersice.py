from random import *


class Exercises(object):
    """
    统计列表中的元素出现次数,按升序排序输出
    """

    @staticmethod
    def exer1(src_list):
        new_list = []
        src_set = set(src_list)
        for n in src_set:
            new_list.append({n: src_list.count(n)})
        new_list.sort(key=lambda d: list(d.values())[0])
        return new_list

    """
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    123
    124
    234
    231
    """
    @staticmethod
    def exer2():
        my_list = [1,2,3,4]
        count = 0
        for i in my_list:
            for j in my_list:
                for k in my_list:
                    if i != j and j != k and i != k:
                        print(f"{i*100 + j*10 + k}")
                        count += 1

        print(count)

    """
    求出100以内的所有素数
    素数: 只能被1和本身除尽的数(1, n)
    """
    @staticmethod
    def exer3():
        count = 0
        for i in range(1,101):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                count += 1
                print(i)

        print(count)

    """
    求出所有三位数中的水仙花数
      水仙花数: 一个三位数,每一位的立方累加和等于该数本身 153 = 1 + 125 + 27
    
    """
    @staticmethod
    def exer4():
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    num = i*100 + j*10 + k
                    my_num = i*i*i + j*j*j + k*k*k
                    if my_num == num:
                        print(num)

    """
    输入若干数字,当输入quit时退出输入,计算输入数字中的最大值,最小值,总和,平均值
    
    """
    # @staticmethod
    # def exer5():
    #     num_list = []
    #     num_sum = 0
    #
    #     while True:
    #         num = input("请输入数字：")
    #
    #         if num == 'quit':
    #             break
    #         num_list.append(num)
    #     count = len(num_list)
    #     if count > 0:
    #         num_max = int(num_list[0])
    #         num_min = int(num_list[0])
    #         for i in num_list:
    #             num_sum += int(i)
    #         for j in range(0,count):
    #             if int(num_list[j]) >= num_max:
    #                 num_max = int(num_list[j])
    #             elif int(num_list[j])<= num_min:
    #                 num_min = int(num_list[j])
    #         avery_num = num_sum/count
    #         print(num_max, num_min, num_sum, avery_num)
    #     else:
    #         print(0,0,0,0)

    @staticmethod
    def exer5():
        count = 0
        sum = 0
        while True:
            data = input("请输入数字：")
            if data.isdigit():
                count += 1
                m = int(data)
                sum += m
                if count == 1:
                    max = m
                    min = m
                else:
                    if m > max:
                        max = m
                    if m < min:
                        min = m
            else:
                if data == 'quit':
                    break
                else:
                    print('非法请重新输入')
        print(max,min,sum,sum/count)

    """
        循环输入若干次字符,输入quit时退出,统计数字,字母,空白,其它字符各有多少(一次只允许输入一个字符)

    """
    @staticmethod
    def exer6():
        number = 0
        character = 0
        space = 0
        other = 0
        while True:
            data = input("请输入一个")
            if data.isdigit():
                number += 1
            elif data.isalpha():
                if data == 'quit':
                    break
                character +=1
            elif data.isspace():
                space += 1

            else:
                other +=1
        print(number,character,space,other)

    """
     输入两个数字 a, b 求s=a+aa+aaa+aaaa+aa...a的值
    例如输入 2, 5
    输出结果 2+22+222+2222+22222 = 24690(此时共有5个数相加)
    输出格式为: x+xx+xx+xx=xxxxx 形式
    """
    @staticmethod
    def exer7():
        sum = 0
        mystr = ''
        num_1 = input("请输入数字一：")
        num_2 = input("请输入数字e二：")
        for i in range(1,int(num_2)+1):
            new_num_1 = num_1 * i
            if i ==1:
                mystr = new_num_1
            mystr = mystr + "+" + new_num_1
            sum += int(new_num_1)

        print(f"{mystr}={sum}")



    """
    自定义实现 int() 
     
    将一个数字字符串转换成真正的数字,并返回
     
    '123'
    """
    @staticmethod
    def exer8():
        sum_num = 0
        num_str = input("请输入一个数字")
        for i in num_str:
            my_num = ord(i) - ord('0')
            sum_num = sum_num * 10 +my_num

        print(sum_num * 10)


    """
    现有 姓氏 和 名字 若干
    设计函数得到一个随机的名字
    """
    @staticmethod
    def exer9():
        fristname = ['周','张','秦']
        sername = ['云','海','慈']
        shuffle(fristname)
        shuffle(sername)

        f_str = fristname[0]
        s_str = sername[0]
        print(f_str + s_str)
    """
    
    利用随机数得到一个随机的字母和数字组成的四位验证码
    然后输入看到的验证码,如果输入正确结束程序,输入错误持续输入直到正确为止
     
    (进阶(作业):如果输入三次不正确,更换验证码后继续)
    """
    @staticmethod
    def exer9():

        i = 1
        s = ''
        while i <= 4:
            n = randint(48,122)
            if(n >= 48 and n <=57) or (n >= 65 and n <=90) or (n >= 97 and n <=122):
                s += chr(n)
                i += 1
        print(s)
        count = 0
        while True:

            my_code = input("请输入验证码：")
            if my_code == s:
                print("正确")
                break
            else:
                count +=1
                print(f"输入错误，错误次数{count}")
                if count == 3:
                    Exercises.exer9()


    """
      求出所有字符串的最小前缀
      a
      ab
      abbc
      abc
      abd
      d 
    """
    @staticmethod
    def exer11():

        old_list = []


        while True:
            my_list = []
            new_list = []
            my_str = input("请输入字符串，输入quit退出")
            if my_str == 'quit':
                break
            else:
                if len(old_list) == 0:
                    for i in my_str:
                        old_list.append(i)
                    continue
                else:
                    for i in my_str:
                        new_list.append(i)
                    length = len(new_list) if len(new_list) <= len(old_list) else len(old_list)

                    for j in range(0,length):
                        if new_list[j] == old_list[j]:
                            my_list.append(new_list[j])

                old_list = my_list
        print(old_list)
    """
    按从高到低的顺序统计文章text中所有单词的使用频率
    
    """
    @staticmethod
    def exer12():
        file_r = open("text.txt", "rt")
        content = file_r.read()
        file_r.close()
        word_list = content.split(' ')
        word_set = set(word_list)
        print(word_set)
        new_list = []

        for n in word_set:
            new_list.append({n: word_list.count(n)})
        new_list.sort(key=lambda d: list(d.values())[0],reverse=True)
        print(new_list)
import keyword
import os
import random
import functools
import  sys
# 单行注释 pycharm快捷键 ctrl+/


'''
    多行注释
    用来描述当前这个程序实现了什么功能
'''
"""
    多行注释
    这个也是注释
"""
'''
print(type(1))
print(type('a'))

print(keyword.kwlist)
'''

'''
['False', 'None', 'True', '__peg_parser__', 'and', 
 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
'''
print('age: %s name:%s' % (10,'nike'))

print('%d' % 1)
print('%3d' % 1)
print('%3d' % 12345)
print('%03d' % 1)
print('%-3d' % 1)

print('%.3f' % 3.12334)
'''

'''
stu_age=10
stu_name='nike'
s=f'age = {stu_age},name={stu_name}'
print(s)
'''

'''
stu_num= input('请输入学号：')
print(stu_num)
'''

'''
stu_grade_1 = input('请输入第一个学生成绩：')
stu_grade_2 = input('请输入第二个学生成绩：')
print(stu_grade_1 + stu_grade_2)
'''

'''
print(10/3)#3.3333333333333335 小数点保留16位
print(10//3)
print(10%3)
print(2**2)
'''

'''
print(int('1')+1)#将字符串1转换成数字1  输出结果为 2
print(int(1.1))#将小数1转换成数字1  输出结果为 1
print(float(1))#将整数1转换成小数1  输出结果为 1.0
print(float('1')+1)#将字符串1转换成小数1  输出结果为 2.0
print(str(1)+'!')#将数字1转成字符串1 输出结果为1！

print(chr(48))#将数字48根据ASCII码转换成对应的字符 输出结果为字符0
print(chr(65))#将数字65根据ASCII码转换成对应的字符 输出结果为字符A
print(chr(97))#将数字97根据ASCII码转换成对应的字符 输出结果为字符a
'''

'''
print(ord('0'))# 48
print(ord('A'))# 65
print(ord('a'))# 97
'''
'''
a=2
b=3.3
c=4
s='a={0:5d} b={1:.3f} c={0}'.format(a,b,c)
print(s)
'''
'''
debug
print(1)
a=1
print(a)
a=10
print(2)
'''
'''
def show():
    print(2)


print(1)
show()
print(3)
'''

"""
def show():
    '''
    show 函数的作用是用来显示一个字符串
    '''

    print(1)#按住crtl建点击函数名即可查看函数说明文档，也可以通过help方法查看


show()

help(show)
"""

'''
def show(num):
    print(num)


show(1)
'''

'''
def get_num():
    a = input('请输入一个数字：')
    return int(a)


print(get_num()//2)

'''

'''
def sum_num(a, b):
    return int(a)+int(b)


print('请输入要计算总和的两个数字：')
a = input()
b = input()
sum_num(a, b)
print(sum_num(a, b))
'''

# print(True and True)

# a = 1
# if a > 10:
#     print('kyi')
# else:
#     print('不可以')


'''
def is_ou(num):
    if num % 2 == 0:
        print(f'{num}是偶数')
    else:
        print(f'{num}不是偶数')


is_ou(2)
'''

'''
def is_week(day):
    if day == 1:
        print(1)
    elif day==2:
        print(2)
'''

'''
n = random.randint(0, 2)
print(n)
'''

'''
def chu_quan(fist):
    if fist == 0:
        return '石头'
    elif fist == 1:
        return '剪刀'
    elif fist == 2:
        return '布'


my = input('请你出拳:(石头：0  剪刀：1  布：2)')
my = int(my)
print(f'你出：{chu_quan(my)}')
com = random.randint(0, 2)
print(f'电脑是{com}')
print(f'电脑出：{chu_quan(com)}')

com = int(com)

if my - com == -1 or my - com == 2:
    print('你赢了')
elif my - com == 1 or my - com == -2:
    print('电脑赢了')
elif my == com:
    print('平局')



'''

'''
# 外3 内5
i = 0
while i < 3:
    j = 0
    while j < 5:
        print('*', end=' ')
        j += 1

    i += 1
    print()  # 换行直接写一个print()
'''

'''
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j:-2d}', end=' ')
        j += 1
    print()
    i += 1
'''

'''
for i in range(1, 9):
    for j in range(1, i+1):
        print(f'{j}*{i}={j*i}', end=' ')
    print()
'''


'''
def my_int(string):
    my_num = 0
    for i in string:

        one_num = ord(i)-ord('0')
        my_num = my_num * 10 + one_num
    return my_num


num = my_int('123')
print(num)
print(num*10)
'''

'''
s = 'hello world'
print(s)  # 切片后不对原字符串产生影响
print(len(s))  # 求字符串长度
print(s[:])  # 复制整个字符串
print(s[2:])  # 从下标2开始到结尾
print(s[:10])  # 从开头到下标2
print(s[1:len(s)])  # 从下标1到字符串长度
print(s[::1])  # 步长默认为1
print(s[::3])  # 每第3个字符一读
print(s[::5])
'''
'''
s = 'hello world'
print(s[::-1])
'''
'''
t = ('a', 1, 2, 3)
for v in t:
    print(v)

for i in range(len(t)):
    print(t[i])

j = 0
while j < len(t):
    print(t[j])
    j += 1
'''
'''
t = ('a', (1, 2, 3), 2, 3, 2)
for v in t:
    if isinstance(v,tuple):
        for v2 in v:
            print(v2)
    else:
        print(v)
print(t.count(2))
print(t.index(2))
'''
'''
t = ['a', (1, 2, 3), 1, [2, 'a']]
for v1 in t:
    if isinstance(v1, tuple):
        for v2 in v1:
            print(v2)
    elif isinstance(v1, list):
        for v3 in v1:
            print(v3)
    else:
        print(v1)
'''
'''

s = 'hello world'
print(s[::-1])

i = 0
s_a = ''
i=len(s)-1
while i >= 0:
    s_a += s[i]
    i -= 1
print(s_a)
'''
'''
 s= 'hello world'
r_list = []
i = len(s)-1
while i >= 0:
    r_list.append(s[i])
    i -= 1

print(r_list)
'''
'''

s = ['h', 'e', 'l' ,'e']
s.insert(5, 'e')
print(s)

print('e' in s)
'''
'''
s = ['h', 'e', 'l', 'e']
s.pop()
print(s)

s.remove('e')
'''
'''
d = {1:'apple',2:'banana'}
for k in d:#使用for - in 循环时，会默认将key遍历
    print(d.get(k))

for k in d.keys():
    print(d.get(k))

for k in d.values():
    print(k)

print(d.items())

for item in d.items():#把每个键子对变成元组
    print(item[0], item[1])

for k ,v in d.items():
    print(k,v)
'''

'''
card = {}


card['name'] = input("名字")
card['age'] = input("名字")
card['address'] = input("名字")

for k in card:
    print(f'{k}:{card.get(k)}')

'''

'''
s = {1,2,3,4,5,5,6}

print(s)
'''

'''
s = {1,2,3,4,5,5,6}

for v in s:
    print(v)
'''

'''
s='hello'
l=set(s)
l1=str(l)
print(l1)
print(len(l1))
print(''.join(l))
print(len(s))
'''
'''
s = []
for i in range(100):
    s.append(i)
'''
'''
s = [i for i in range(100)]
s = [i for i in range(100) if i % 2 == 0]
s = [(x, y)for x in range(10) for y in range(3)]

print(s)
print(len(s))

'''
'''
#组包
a = 1, 2, 3, 4, 5 #元组
print(a)
print(type(a))
#拆包
# a1, a2, a3, a4, a5 = a
# a1, a2, a3, a4, a5 = 'abcdx'
# a1, a2, a3, a4, a5 = [1,2,3,4,5]
a1, a2 = {'a': 1, 'b': 2}
print(a1, a2)
'''
'''
def get_max_min(m_list):
    i = len(m_list)-1
    max = m_list[0]
    min = m_list[0]
    while i >= 0:
        if max < m_list[i-1]:
            max = m_list[i-1]
        elif min > my_list[i-1]:
            min = m_list[i]
        i -= 1
    return max, min

my_list = [2,3,6,9]
t = get_max_min(my_list)

for v in t:
    print(v)
'''
'''
def factoria(n):
    if n == 1:
        return 1
    return n*factoria(n-1)


print(factoria(3))

'''
# map
# lambda m, n: m if m > n else n
'''
def map(func, m_list):
    all_list = []
    for i in m_list:
        result = func(i)
        all_list.append(result)
    return all_list


new_list = map(lambda x: x**2, [1,2,3,4])
for j in new_list:
    print(j)
'''
'''
my_list = list('hello')

result = functools.reduce(lambda x1,x2: x1.upper() + x2.upper(),my_list)
print(result)
'''
'''
my_list = [1,2,3,4,5]
result = functools.reduce(lambda n1,n2:n1*n2,my_list)
print(result)
'''

'''
my_list = ['123','avc','12b','-ds','-23','234']

num_list = filter(lambda  s: s.isdigit(),my_list)
for s in list(num_list):
    print(s)
'''
'''
my_list = [{'id':1,'name':'tom','age' : 12},{'id':3,'name':'som','age' : 12},{'id':2,'name':'tom','age' : 12}]

my_list.sort(key=lambda d : d['name'],reverse=True)
print(my_list)
'''
'''
# 文件操作

file = open('a.txt', 'rt')
# content = file.read()

while True:
    content = file.read(1)
    if content == '':
        break
    print(content)

# print(content)
file.close()
'''

'''
def file_copy(src,dst):

    file_r = open(src,'r')
    file_w = open(dst,'w')
    while True:
        content = file_r.read(4096)

        if content == '':
            print("拷贝成功")
            break
        file_w.write(content)
    file_r.close()
    file_w.close()

print(sys.argv)
src = sys.argv[0]
dst = sys.argv[1]
file_copy(src,dst)
'''

'''
def file_copy(src,dst):

    file_r = open(src,'rb')
    file_w = open(dst,'wb')
    while True:
        content = file_r.read(4096)

        if content == b'':
            print("拷贝成功")
            break
        file_w.write(content)
    file_r.close()
    file_w.close()

print(sys.argv)
src = sys.argv[0]
dst = sys.argv[1]
file_copy(src,dst)
'''

'''
# 批量读取文件，改名之后复制
def muilt_file_copy(src,dst):
    # os.mkdir(dst)
    os.chdir(src)
    print(os.getcwd())
    file_list = os.listdir('.')

    #print(file_list)
    for file in file_list:
        s_file = file.rpartition('.')
        # print(s_file)
        dst_file = dst + '/' + s_file[0] + '_1' + s_file[1] + s_file[2]
        # print(dst_file)
        file_r = open(file,'rt')
        file_w = open(dst_file,'wt')

        while True:
            content = file_r.read(4096)
            if content == '':
                print(f"{file}复制超过")
                file_r.close()
                file_w.close()
                break
            file_w.write(content)
        else:
            print(f"一共复制了{len(file_list)}个文件")


src = 'C:/Users/yoki/Desktop/vv'

dst = 'C:/Users/yoki/Desktop/v'

muilt_file_copy(src,dst)
'''

# 把一个文件夹下的所有文件进行批量重命名并复制到另一个文件夹中
'''
def all_copy_rename(src,dst):
    os.chdir(src)
    print(os.getcwd())

    file_list = os.listdir('.')
    for file in file_list:

        p_file = file.rpartition('.')
        dst_file = dst + '/' + p_file[0]+'--'+p_file[1]+p_file[2]
        print(dst_file)
        file_r = open(file,'rt')
        file_w = open(dst_file,'wt')

        while True:
            content = file_r.read(1024)
            if content == '':
                print(f"{file}复制成功")
                file_w.close()
                file_r.close()
                break
            file_w.write(content)
        else:
            print(f"一共复制了{len(file_list)}")


src = "C:/Users/yoki/Desktop/vv"
dst = "C:/Users/yoki/Desktop/v"
all_copy_rename(src,dst)
'''


'''
class Human(object):

    def eat(self,food):
        print(self.name,"在吃",food)


tom = Human()

tom.name = 'Tom'
tom.eat("苹果")

rose = Human()
rose.eat("香蕉")
'''

'''
class Dog(object):
    def __init__(self,name,age,height):

        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(self.name,self.age)

    def __str__(self):
        s = self.name.ljust(10) + str(self.age).ljust(5) + self.height.ljust(10)
        return s

    def __del__(self):
        del self.name
        print('del')

tom = Dog('To',1,'10cm')
print(str(tom))

del tom
print("over")
'''

'''
class Potato(object):
    def __init__(self):
        self.state = "生瓜"
        self.time = 0
        self.tl = []

    def cook(self,t):
        self.time += t

        if self.time <3:
            self.state = '还是生的'
        elif self.time < 6:
            self.state = '半生不熟'
        elif self.time < 8:
            self.state = '刚刚好'
        else:
            self.state = '烤糊了'

    def __str__(self):

        s = self.state + f'被烤了{self.time}分钟'
        s += '地瓜使用了：\n'
        for i in self.tl:
            s += (i+ '\n')
        return s

    def add_tl(self, t):
        self.tl.append(t)
potato = Potato()


potato.cook(2)
print(potato)
potato.cook(3)
potato.add_tl("芝麻")

print(potato)
potato.cook(3)
potato.add_tl("孜然")
print(potato)
'''


'''
class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self,n):
        print('汪'*n)


class Human(object):
    def __init__(self,name ,age):
        self.name = name
        self.age = age

    def add_pet(self,pet):
        self.pet = pet

    def listen_dog_bark(self,time):
        self.pet.bark(time)


tom = Human('Tom', 23)
tom.add_pet(Dog('diandian',4))
tom.listen_dog_bark(3)

'''

class Phone(object):
    def call(self,number):
        print(f"正在给{number}打电话")


class iPhone(Phone):

    def camera(self):
        print("paizhao")

iPhonex = iPhone()
iPhonex.call("18166041567")
iPhonex.camera()
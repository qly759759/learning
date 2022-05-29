from student import *


class StudentManagerSystem(object):

    def __init__(self):
        self.students = {}
        self.__load_data()

    def start(self):
        print("success")
        while True:
            self.__print_menu()
            select_id = input("请输入要选择功能的ID：")
            if select_id.isdigit():
                n = int(select_id)
                if n >= 1 and n <= 6:
                    self.__operator(select_id)
                else:
                    print("超过范围")
            else:
                print("输入非法功能，重新输入")

    def __print_menu(self):
        print("1.增加")
        print("2.删除")
        print("3.修改")
        print("4.查找")
        print("5.显示全部")
        print("6.退出系统")

    def __operator(self, select_id):
        print('选择了功能：', select_id)
        method_dict = {'1': self.__add_stu,
                       '2': self.__del_stu,
                       '3': self.__modify_stu,
                       '4': self.__search_stu,
                       '5': self.__all_stu,
                       '6': exit}
        method = method_dict[select_id]

        if select_id == '3' or select_id == '4' or select_id == '2':
            stu_id = input('请输入要操作的学生ID')
            method(stu_id)
        elif select_id == '6':
            self.__save_data()
            method(0)
        else:

            method()

    def __add_stu(self):
        print('添加学生')
        stu_info = self.__input_stu()
        stu = Student(stu_info[0], stu_info[1], stu_info[2])
        self.students[stu.stu_id] = stu
        print(self.students)

    def __search_stu(self, stu_id):
        print(stu_id)
        stu = None
        if stu_id in self.students.keys():
            print("key", self.students.keys())
            stu = self.students[stu_id]
            self.__show_info(stu)
        else:
            print("key", self.students.keys())
            print("bucunzai")
        return stu

    def __modify_stu(self, stu_id):
        stu = self.__search_stu(stu_id)
        if stu is not None:
            # self.__del_stu(stu_id)
            new_stu_info = self.__input_stu()
            stu.stu_id = new_stu_info[0]
            stu.stu_name = new_stu_info[1]
            stu.stu_age = new_stu_info[2]

            # self.students[stu.stu_id] = stu

            self.__show_info(stu)
        else:
            print('要修改的学生', stu_id)

    def __del_stu(self, stu_id):
        stu = self.__search_stu(stu_id)
        if stu is not None:
            self.students.pop(stu_id)
        else:
            print("没找到")

    def __show_info(self, stu):
        print(stu)

    def __all_stu(self):
        for stu in self.students.values():
            self.__show_info(stu)

    def __input_stu(self):
        stu_id = input("请输入学生的ID")
        stu_name = input("请输入学生的姓名")
        stu_age = input("请输入学生的年龄")
        return stu_id, stu_name, stu_age

    def __save_data(self):
        print('保存数据')
        # 以行的形式来保存每一个学生的信息

        # 以写的方式打开一个文件
        file_w = open('data', 'w')

        # 遍历所有的学生信息
        for stu in self.students.values():
            # 将学生转换成一个学生字符串对象
            # stu_s = str(stu)
            stu_s = stu.stu_id + ' ' + stu.stu_name + ' ' + stu.stu_age + '\n'
            # print(stu_s)

            # 将学生信息组织成一个固定格式的字符串,按行写入到文件中
            file_w.write(stu_s)

        # 关闭文件
        file_w.close()

    # 加载数据
    def __load_data(self):
        print('加载数据')
        # 打开文件,并要处理文件不存在的异常
        file_r = None
        try:
            file_r = open('data', 'r')
        except Exception as e:
            print(e, '文件不存在')
        else:
            # 读取文件内容,按行读取
            content = file_r.readlines()

            # 遍历每一行数据
            for stu_s in content:
                split_info = stu_s.split()

                # 创建一个学生对象,然后保存到字典里
                stu = Student(split_info[0], split_info[1], split_info[2])
                # 加到字典里
                self.students[stu.stu_id] = stu
        finally:
            if file_r != None:
                file_r.close()

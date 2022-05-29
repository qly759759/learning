
stu_list = list()

def show():
    print("1.增加")
    print("2.删除")
    print("3.修改")
    print("4.查找")
    print("5.显示全部")
    print("6.退出系统")


def control(c_id):
    if c_id == '1':
        add_stu()
    elif c_id == '2':
        del_id = input("请输入你要删除的学号：")
        del_stu(del_id)
    elif c_id == '3':
        modify_id = input("请输入你要x修改的学号：")
        modify_stu(modify_id)
    elif c_id == '4':
        stu_id = input("请输入你要查找的学号：")
        find_one_stu(stu_id)
    elif c_id == '5':
        find_all()
    elif c_id == '6':
        exit(0)
    else:
        print(f"没有序号为{c_id}的操作")


def main():
    while True:
        show()
        c_id = input("请输入你要进行的操作序号：")
        control(c_id)


def input_info():
    stu_id = input("请输入学生id：")
    stu_name = input("请输入学生姓名：")
    stu_age = input("请输入学生年龄：")
    return stu_id,stu_name,stu_age


def add_stu():
    stu = {}
    stu_info = input_info()
    stu['id'] = stu_info[0]
    stu['name'] = stu_info[1]
    stu['age'] = stu_info[2]
    stu_list.append(stu)
    show_one_stu(stu)


def del_stu(del_id):
    stu = find_one_stu(del_id)
    if stu is not None:
        stu_list.remove(stu)


def modify_stu(modify_id):
    stu = find_one_stu(modify_id)
    if stu is not None:
        stu_info = input_info()
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['age'] = stu_info[2]
        show_one_stu(stu)


def show_one_stu(stu):
    print(f"{stu['id']},{stu['name']},{stu['age']}")


def find_one_stu(stu_id):
    for stu in stu_list:
        if stu_id == stu['id']:
            show_one_stu(stu)
            return stu
    else:
        print(f"不存在学号为{stu_id}的同学")
        return None


def find_all():
    for stu in stu_list:
        show_one_stu(stu)


main()
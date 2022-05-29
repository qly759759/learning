
student = []

def show_info():
    print("1.增加")
    print("2.删除")
    print("3.修改")
    print("4.查找")
    print("5.显示全部")
    print("6.退出系统")


def main():
    while True:
        show_info()
        select_id = input("请输入你要进行的操作")
        operator_stu(select_id)


def operator_stu(select_id):
    if select_id == '1':
        add_stu()
    elif select_id == '2':
        del_id = input("请输入要删除的学号：")
        del_stu(del_id)
    elif select_id == '3':
        modify_id = input("请输入要修改的学号：")
        modify(modify_id)
    elif select_id == '4':
        find_id = input("请输入要查找的学号：")
        find_stu(find_id)
    elif select_id == '5':
        show_all()
    elif select_id == '6':
        exit()


def add_stu():
    stu = {}#需要改成字典{}
    stu_info = input_stu_info()#接收的是元组（）
    stu['id'] = stu_info[0]
    stu['name'] = stu_info[1]
    stu['age'] = stu_info[2]
    student.append(stu)
    show_one_stu(stu)


def input_stu_info():
    stu_id = input("请输入id")
    stu_name = input("请输入姓名")
    stu_age = input("请输入年龄")
    return stu_id, stu_name, stu_age


def show_one_stu(stu):
    print(f"学号：{stu['id']},姓名：{stu['name']},年龄：{stu['age']}")


def del_stu(del_id):
    stu = find_stu(del_id)
    if stu is not None:
        student.remove(stu)


def modify(modify_id):
    stu = find_stu(modify_id)
    if stu is not None:
        stu_info = input_stu_info()
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['age'] = stu_info[2]

        show_one_stu(stu)


def show_all():
    for stu in student:
        if stu is not None:
            show_one_stu(stu)
        else:
            print("没有学生")


def find_stu(find_id):
    for stu in student:
        if find_id == stu['id']:
     
            show_one_stu(stu)
            return stu
        else:
            print(f"不存在学号为{find_id}的同学")
            return None


main()
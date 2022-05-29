student = []


def main():
    while True:
        show_menu()
        select_id = input('请输入你要选择的操作')
        operator(select_id)


# 显示菜单
def show_menu():
    print("1.增")
    print("2.删")
    print("3.改")
    print("4.查询")
    print("5.显示所有学生")
    print("6.退出系统")


# 功能选择函数
def operator(select_id):
    if select_id == '1':
        add_stu()
    elif select_id == '2':
        del_id = input('请输入你要删除的id:')
        del_stu(del_id)
    elif select_id == '3':
        modify_id = input('请输入你要修改的id:')
        modify_stu(modify_id)
    elif select_id == '4':
        find_id = input('请输入你要查找的id:')
        find_stu(find_id)
    elif select_id == '5':
        show_all()
    elif select_id == '6':
        exit()
    else:
        print('输入的ID错误，请重新输入')


def in_put_stu():
    stu_id = input("请输入学号")
    stu_name = input("请输入姓名")
    stu_age = input("请输入年龄")
    return stu_id, stu_name, stu_age


def add_stu():
    stu = {}  # 字典
    stu_info = in_put_stu()
    stu['id'] = stu_info[0]
    stu['name'] = stu_info[1]
    stu['age'] = stu_info[2]
    student.append(stu)



def find_stu(stu_id):
    for stu in student:
        if stu['id'] == stu_id:
            show_one_stu(stu)
            return stu
    else:
        print(f'未找到学号为{stu_id}的学生')
        return None


# 显示单个学生信息的函数
def show_one_stu(stu):
    print(f"学号：{stu['id']},姓名:{stu['name']}，年龄:{stu['age']}")


def del_stu(del_id):
    stu = find_stu(del_id)
    if stu != None:
        student.remove(stu)
        print(f"已删除{del_id}学生")


def modify_stu(modify_id):
    stu = find_stu(modify_id)
    if stu != None:
        stu_info = in_put_stu()
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['age'] = stu_info[2]
        show_one_stu(stu)


def show_all():
    for stu in student:
        show_one_stu(stu)

main()

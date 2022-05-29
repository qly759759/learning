
student = []
# 显示菜单
def show():

        print("1.增加")
        print("2.删除")
        print("3.修改")
        print("4.查找")
        print("5.显示所有")
        print("6.退出系统")


def operator(operator_id):

    if operator_id == "1":
        add_stu()
    elif operator_id == "2":
        del_id = input("请输入你要删除的id")
        del_stu(del_id)
    elif operator_id == "3":
        modify_id = input("请输入你要修改的id")
        modify_stu(modify_id)
    elif operator_id == "4":
        find_id = input("请输入你要查找的id")
        find_stu(find_id)
    elif operator_id == "5":
        show_all()
    elif operator_id == "6":
        exit()
    else:
        print("不存在此操作")



def main():
    while True:
        show()
        op_id = input("请输入你要进行的操作序号：")
        operator(op_id)


def input_stu_info():
    stu_id = input("请输入学号：")
    stu_name = input("请输入姓名：")
    stu_age = input("请输入年龄：")
    return stu_id, stu_name, stu_age


def add_stu():
    stu = {}
    stu_info = input_stu_info()
    stu['id'] = stu_info[0]
    stu['name'] = stu_info[1]
    stu['age'] = stu_info[2]
    student.append(stu)
    show_one_info(stu)


def show_one_info(stu):
    print(f"学号：{stu['id']},姓名：{stu['name']},年龄:{stu['age']}")


def find_stu(find_id):
    for stu in student:
        if stu["id"] == find_id:
            return stu
            show_one_info(stu)
        else:
            print(f"不存在学号为：{stu['id']}的学生")
            return None


def show_all():
    for stu in student:
        if stu is not None:
            show_one_info(stu)
        else:
            print("没有学生")






def del_stu(del_id):

    stu = find_stu(del_id)
    if stu is not None:
        student.remove(stu)


def modify_stu(modify_id):
    stu = find_stu(modify_id)
    if stu is not None:
        stu_info = input_stu_info()
        stu['id'] = stu_info[0]
        stu['name'] = stu_info[1]
        stu['age'] = stu_info[2]

main()

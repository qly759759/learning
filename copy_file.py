import os

def copy_file(src, dst):
    print(os.getcwd())
    os.chdir(src)

    file_list = os.listdir('.')
    for file in file_list:

        p_file = file.rpartition('.')
        dst_file = dst+ '/' + p_file[0] + '-1' + p_file[1] + p_file[2]
        file_r = open(file,'rt')
        file_w = open(dst_file,'wt')

        while True:
            content = file_r.read(1024)
            if content == '':
                file_r.close()
                file_w.close()
                print(f"{file}复制成功")
                break
            file_w.write(content)
    print(f"一共复制了{len(file_list)}")


src = "C:/Users/yoki/Desktop/src"
dst = "C:/Users/yoki/Desktop/dst"
copy_file(src, dst)
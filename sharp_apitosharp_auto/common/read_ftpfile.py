import os
# 项目路径
pro_path = os.path.split(os.path.split(os.path.realpath(__file__),)[0])[0]
# 获取包括文件名的sa的完整路径
sa_dir_path = os.path.join(pro_path, "ftp_file", "sa_from_jusda_file")
sa_filename = os.listdir(sa_dir_path)[0]
sa_file_path = os.path.join(sa_dir_path,sa_filename)
# 获取包括文件名的纳品的完整路径
deli_dir_path = os.path.join(pro_path, "ftp_file", "delivery_file")
deli_filename = os.listdir(deli_dir_path)[0]
deli_file_path = os.path.join(deli_dir_path, deli_filename)

def read_sa_file():
    
    with open(sa_file_path,"r", encoding="utf-8") as file:
        lines = file.readlines()
        # print(lines)
        return(lines)


def read_deli_file():
    
    with open(deli_file_path,"r",encoding="utf-8") as file:
        lines = file.readlines()
        # print(lines)
        return(lines)



if __name__ == '__main__':
    print(read_deli_file())


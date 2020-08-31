import os
pro_path = os.path.split(os.getcwd())[0]
sa_dir_path = os.path.join(pro_path, "ftp_file", "sa_from_jusda_file")
filename = os.listdir(sa_dir_path)[0]
sa_file_path = os.path.join(sa_dir_path,filename)
def read_sa_file():
    sa_data_list=[]
    with open(sa_file_path,"r") as file:
        lines = file.readlines()
        print(lines)
        return(lines)

if __name__ == '__main__':
    # 数据部分
    data_list = [
        "SAHD 00000000     20081812274400000            SHARP                                                                            \n",
        "SA02100010001        20200818            20200818             000000000000000000000000002008180000000016787SHANGHAI Y           \n"]
    # 切割的长度，依此为标准
    stand = {"SAHD ": [4,1,4,4,5,6,6,5,6,6,6]}
    # 处理模块
    # 切割后的内容放在列表中，待做判定
    data_split_result = []
    for i in range(0,len(stand["SAHD "])):
        length = stand["SAHD "][i]
        start_no=0
        if i >= 1:
            for j in range(0, i):
                start_no += stand["SAHD "][j]

        data_split_result.append(data_list[(start_no):(start_no+length)])

    print(data_split_result)
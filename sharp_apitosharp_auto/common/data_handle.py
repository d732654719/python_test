from common.read_ftpfile import read_sa_file,read_deli_file

stand_sa = {
    "SAHD ": [4, 1, 4, 4, 5, 6, 6, 5, 6, 6, 6],
    "SA021": [4, 1, 4, 4, 1, 7, 20, 20, 1, 13, 13, 6, 13, 10, 10, 1],
    "SA022": [4, 1, 4, 4, 1, 6, 6, 25, 4, 10, 5, 5, 6, 6, 5, 4],
    "SA023": [4, 1, 4, 4, 13, 2, 3, 1, 13, 2, 3, 1, 13, 1, 3, 6, 13],
    "SA03 ": [4, 1, 4, 4, 1, 7, 4, 2, 4, 4, 4, 1, 9, 3, 1, 1, 13, 1, 3, 13, 13, 13, 13, 2],
    "SA041": [4, 1, 4, 4, 1, 7, 2, 14, 9, 13, 13, 15, 5, 2, 7, 13, 13],
    "SA042": [4, 1, 4, 4, 7, 9, 7, 9, 7, 9, 7, 9, 7, 9, 4, 13, 13],
    "SA05 ": [4, 1, 4, 4, 1, 7, 2, 7, 1, 4, 4, 9, 9, 9, 7, 1, 3],
    "SA99 ": [4, 1, 4, 4, 5]
}

stand_deli = {
    "GK30": [4, 8, 2, 2, 4, 10, 2, 10, 2, 2, 14, 3, 1, 6, 4, 1, 8, 5, 1, 16, 10, 6, 6, 1, 1, 15, 11, 11, 1, 3, 3, 3, 1,
             1, 3, 1, 2, 1, 1, 8, 6, 3, 2, 5, 4, 3, 2, 5, 4, 1, 25, 8, 5, 10, 15, 11, 10, 9, 20, 10, 11, 10, 11, 10, 1,
             3, 8, 8, 1, 40, 40, 1, 25, 1, 7, 5, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 8, 8, 8, 10, 18, 18, 18, 18,
             18, 18, 18, 18, 18, 18, 3, 18, 4, 2, 8]}



# 处理模块,切割后的内容放在列表中，待做判定
def sa_after_split(data_choosed):
    data_split_result = []
    two_dimen_data=[]
    # 用于匹配分割标准的字符串
    flag = data_choosed[0:5]
    for i in range(0, len(stand_sa[flag])):
        length = stand_sa[flag][i]
        start_no = 0
        if i >= 1:
            for j in range(0, i):
                start_no += stand_sa[flag][j]

        data_split_result.append(data_choosed[(start_no):(start_no + length)])
    return data_split_result

def deli_after_split(data_choosed):
    data_split_result = []
    # 用于匹配分割标准的字符串
    flag = data_choosed[0:4]
    for i in range(0, len(stand_deli[flag])):
        length = stand_deli[flag][i]
        start_no = 0
        if i >= 1:
            for j in range(0, i):
                start_no += stand_deli[flag][j]

        data_split_result.append(data_choosed[(start_no):(start_no + length)])
    return data_split_result

def gener_complete_sa_list():
    complete_sa_list=[]
    datalist = read_sa_file()
    for i in datalist:
        complete_sa_list.append(sa_after_split(i))
    return complete_sa_list

def gener_complete_deli_list():
    comple_list=deli_after_split(read_deli_file()[0])
    return comple_list

if __name__ == '__main__':
    a=gener_complete_sa_list()
    print(a)
        

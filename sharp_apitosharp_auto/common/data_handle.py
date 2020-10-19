from common.read_ftpfile import read_sa_file, read_deli_file
import re

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

stand_len_sa = {
    "SAHD ": 53,
    "SA021": 128,
    "SA022": 96,
    "SA023": 87,
    "SA03 ": 125,
    "SA041": 127,
    "SA042": 123,
    "SA05 ": 77,
    "SA99 ": 18
}
# 计算出含有中日，中文标点符号等占两个字符的line的字节长度
def count_linelength(line):

    # line = '20200901 輸入完成品・23空調（ＳＴＣ）'
    byte2 = re.compile('[\u4e00-\u9fff\u30a0-\u30ff\u3040-\u309f\u3000-\u303f\ufb00-\ufffd]+').findall(line)
    byte2length = 0
    for i in byte2:
        byte2length += len(i)
    line_length = len(line)+byte2length
    return line_length

# 判断sa数据的是否符合标准长度1:53,2:128,3:96,4:87,5:125,6:127,7:123,8:77,9:18
# def saLineslength_aseert():
#     lines = read_sa_file()
#     rows_num = len(lines)
#     r = 0
#     errorlines=[]
#     for i in range(0, len(lines)):
#         flag = read_sa_file()[i][0:5]
#         if count_linelength(read_sa_file()[i]) == stand_len_sa[flag]:
#             r += 1
#         else:
#             j = i + 1
#             errorlines.append(j)
#     if r == rows_num:
#         return 'True'
#     else:
#         return '第{}行不符合标准长度'.format(errorlines)

# 判断纳品数据是否符合标准长度
def deliLineslength_assert():
    lines = read_deli_file()
    rows_num = len(lines)
    r = 0
    errorlines=[]
    for i in range(0, len(lines)):
        if count_linelength(read_deli_file()[i]) == 813:
            r += 1
        else:
            j = i+1
            errorlines.append(j)
    if r == rows_num:
        return 'True'
    else:
        return '第{}行不符合标准长度'.format(errorlines)

def findall_2byte(s, cut_len):
    '''
    查找字符串中的所有中日，中文标点符号，将切片长度剪掉等长
    :param s: 待查找字符串
    :return: 处理后的切片长度
    '''

    s_after_math = re.compile('[\u4e00-\u9fff\u30a0-\u30ff\u3040-\u309f\u3000-\u303f\ufb00-\ufffd]+').findall(s)
    if s_after_math is not None:
        # print(s_after_math)
        leng = 0
        for i in s_after_math:
            leng += len(i)
        cut_len = cut_len - leng
        # print("切割长度：{},切割后长度{}".format(leng,cut_len))
        return cut_len
    else:
        # print("不需要切：{}".format(cut_len))
        return cut_len


# 处理模块,切割后的内容放在列表中，待做判定
def sa_after_split(data_choosed):
    data_split_result = []
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

        if i == 69:
            length = findall_2byte(data_choosed, stand_deli[flag][69])
            stand_deli[flag][69] = length
        if i >= 1:
            for j in range(0, i):
                start_no += stand_deli[flag][j]
        data_split_result.append(data_choosed[(start_no):(start_no + length)])

    return data_split_result


def gener_complete_sa_list():
    complete_sa_list = []
    datalist = read_sa_file()
    for i in datalist:
        complete_sa_list.append(sa_after_split(i))
    return complete_sa_list


def gener_complete_deli1_list():
    comple_list = deli_after_split(read_deli_file()[0])
    return comple_list


def gener_complete_deli_list():
    complete_deli_list = []
    datalist = read_deli_file()
    for i in datalist:
        complete_deli_list.append(deli_after_split(i))
        stand_deli["GK30"][69] = 40
    return complete_deli_list


if __name__ == '__main__':
    print(gener_complete_deli_list())

import math
#计算信息熵，p代表一件事发生的改路，统计一件事的所有可能性的概率填入函数中，即可计算信息熵
def info_entropy( *p):
    ie = 0
    for i in p:
        ie += float(i)*(-(math.log(i,2)))
    print(ie)
    return ie

ie = info_entropy(0.5,0.5)



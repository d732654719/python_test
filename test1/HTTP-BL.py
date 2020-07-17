import requests
import json
def getToken():
    method = "POST"
    params = {
            "grant_type":"password",
            "username": "alex",
            #"username": "Daniel",
            #"password": "948542b99a45de7ced6b6df6830dbb0a",
            #"password": "518d1b4825b18a38d48771fb9dbad71d",
            "password": "e6f41bad2eebe58b8147ec36597a824e",
            "tenant_code": "SHARP"
        }
    header = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "authorization": "Basic Y2xpZW50OjYyNjA4ZTA4YWRjMjlhOGQ2ZGJjOTc1NGU2NTlmMTI1",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",

    }
    # url = "https://sharpsit.jusdaglobal.com/api/login"
    url = "https://sharpuat.jusdaglobal.com/api/login"
    #url ="https://sls.sccpcloud.com/api/login"
    rep = requests.request(method, url, data=params,headers= header)
    r =json.loads(rep.text)
    token = "Bearer "+ r["access_token"]
    return token


token =getToken()
# url = "https://sharpsit.jusdaglobal.com/api/shipping-advices"
url = "https://sharpuat.jusdaglobal.com/api/shipping-advices"
# url ="https://sls.sccpcloud.com/api/shipping-advices"


header = {
        "content-type": "application/json;charset=UTF-8",
        "accept": "application/json, text/plain, */*",
        "authorization": token
}
#以do为检索条件返回搜索数量
def get_num_by_do(do,url=url,header=header):
    params = {
        "view": "B1600",
        # "partnerId":"11698d03-5214-444c-9cdc-5594db28e26e",
        "doNo" :do,
        "size": 10,
        "sort": "doNo,desc",
        "page": i
    }
    result = requests.get(url, params, headers=header)
    result = json.loads(result.text)
    return len(result.content)

#获取一页中的do作为列表
def getdo_list_1page(url,params,header):
    result = requests.get(url, params, headers=header)
    result = json.loads(result.text)
    # # print(len(result["content"]))
    # # print(type(result["content"][0]["doNo"]))
    doNo_list = []
    length = len(result["content"])
    # print(length)
    for j in range(0, length):
        if result["content"][j]["doNo"] is not None:
            doNo = result["content"][j]["doNo"]
            doNo_list.append(doNo)
    return doNo_list


# 查询列表数据是否有重复
def check_rep(list):
    print(len(list))
    lista = set(list)
    print(len(lista))

# 查询一个列表中哪些数据重复
def witch_rep(list):
    rep_list =[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                rep_list.append(list[i])
    print(rep_list)
# 查询两个列表中哪些数据重复,并以list返回他们
def witch_rep_page(list1,list2):
    rep_list =[]
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                rep_list.append(list1[i])
    set_l = set(rep_list)
    print(set_l)
    return list(set_l)
# witch_rep(doNo_list)

for i in (-1,1,2,3,4,5,6,7,8,9,10,11,12,13):
    for k in range(i+1, 13):
        params_1 = {
            "view": "B1600",
            "blIssueDateFrom": "2019-11-15",
            "blIssueDateTo": "2020-03-01",

            # "partnerId":"11698d03-5214-444c-9cdc-5594db28e26e",
            "size": 10,
            "sort": "doNo,desc",
            "page": i
        }
        params_2 = {
            "view": "B1600",
            "blIssueDateFrom": "2019-11-15",
            "blIssueDateTo": "2020-03-01",

            # "partnerId": "11698d03-5214-444c-9cdc-5594db28e26e",
            "size": 10,
            "sort": "doNo,desc",
            "page": k
        }

        # 相同页数即同一页面，不必比较,和跳过k=0的情况
        if i == k or k==0:
            continue
        # 获取相邻页的数据
        do_page1 = getdo_list_1page(url, params_1, header)
        do_page2 = getdo_list_1page(url, params_2, header)
        # 跳过整个页面没有一个数据有do的页面
        if do_page1 == [] or do_page2 ==[]:
            continue
        # 按页为单位，相互比较每一页的数据
        print("第{}页:{}".format(i,do_page1))
        print("第{}页:{}".format(k,do_page2))
        # 查询两个列表中哪些数据重复,并以list返回他们
        l = witch_rep_page(do_page1, do_page2)
        # 等于一的有问题，就是重复数据，将其输出
        # for a in l:
        #     if get_num_by_do(a) == 1:
        #         print(a)

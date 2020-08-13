import requests, logging, json

def http_requests(method,url,headers,params,files):
    try:
        response = requests.request(method=method,url=url,headers=headers,params=params,files=files)
        return response
    except Exception as e:
        logging.error("请求参数出错，错误信息：".format(e))
        raise e

if __name__ == '__main__':
    data={'用例编号': 1, '用例名称': '登录接口', '请求方式': 'POST', '接口地址': 'https://sharpsit.jusdaglobal.com/api/login',
      '请求头': '{"content-type":"application/x-www-form-urlencoded;charset=UTF-8","authorization":"Basic Y2xpZW50OjYyNjA4ZTA4YWRjMjlhOGQ2ZGJjOTc1NGU2NTlmMTI1"}',
      '请求参数': '{"grant_type":"password","username":"alex","password":"948542b99a45de7ced6b6df6830dbb0a","tenant_code":"SHARP"}',
      '文件参数':  "''"}
    method = data["请求方式"]
    url = data["接口地址"]
    header = eval(data["请求头"])
    params = eval(data["请求参数"])
    files = eval(data["文件参数"])
    resp = http_requests(method, url, header, params, files)
    print(resp)

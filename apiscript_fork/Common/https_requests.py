import requests, logging, json

def http_requests(method,url,headers,params,files):
    try:
        response = requests.request(method=method,url=url,headers=headers,params=params,files=files)
        return response
    except Exception as e:
        logging.error("请求参数出错，错误信息：".format(e))
        raise e
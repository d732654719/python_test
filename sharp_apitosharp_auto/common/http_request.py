import requests
import json
def http_request(url,method,header,data):
    try:
        data=json.loads(data)
        result = requests.request(method,url,headers=header,data=data)
        # result返回全部，调用后要做处理
        return result
    except Exception as e:
        raise e

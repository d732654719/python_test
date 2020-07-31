import logging,re
from jsonpath import jsonpath


def value_by_jsonpath(json_obj,expr):
    """
    从json格式的数据中，返回jsonpath表达式指定的值
    :param json_obj:
    :param expr:
    :return: 返回json_obj被expr解析后的值或列表
    """
    value = jsonpath(json_obj,expr)
    if value:
        if len(value) > 1:
            result = value
        else:
            result = value[0]
    else:
        logging.error("你的查找这可能是None或者是false，或查看你的jsonpath是否正确")
        result = value
    return result


def repl_jsonpth(repl,dict_json):
    """
    替换jsonpath表达式
    :param repl: 含jsonpath表达式的url，请求参数，文件参数，请求头，全局变量，预期结果
    :param dict_json:被取值的json数据
    :return: jsonpath被替换后的字符串
    """
    try:
        while re.search("\{(\$.*?)\}",repl):
            replaced_str = re.search("\{(\$.*?)\}",repl).group()
            json_path = re.search("\{(\$.*?)\}",repl).group(1)
            value = value_by_jsonpath(dict_json,json_path)
            repl = repl.replace(replaced_str,value)
        return repl
    except TypeError:
        logging.error("excel中被替换数据中的jsonpath格式可能有问题，请检查")
        return repl


if __name__ == '__main__':
    data = {"sort": True, "data": False, "success": None, "code": "sb9999",
            "ids": [["abc"], ["ttt"]], "user": {"name": "tom", "age": 23}}
    rep = '{"username":"{$ids[0][0]}","password":"{$.code}","clientId":"visual"}'
    result = repl_jsonpth(rep, data)
    print(result)

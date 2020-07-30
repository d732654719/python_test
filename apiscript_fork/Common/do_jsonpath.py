import logging
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
        if len(value)>1:
            result = value
        else :
            result = value[0]
    else:
        logging.error("你的查找这可能是None或者是false，或查查看你的jsonpath是否正确")
        result = value
    return result

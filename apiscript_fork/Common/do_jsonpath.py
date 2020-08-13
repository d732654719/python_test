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
        logging.error("你的查找值可能是None或者是false，或查看你的jsonpath是否正确")
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
    data = {'access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3VudHJ5X2NvZGUiOiJKUCIsImxvY2FsZV9jb2RlIjoiZW5fVVMiLCJ1c2VyX25hbWUiOiJhbGV4Iiwic2NvcGUiOlsiZm9vIiwicmVhZCIsIndyaXRlIl0sImFwcGxpY2F0aW9uX2NvZGUiOiJJREVBUyIsImV4cCI6MTU5NjU0Nzg1NywidXNlcmFjY291bnRfaWQiOiJVQUNfMTAwNDczIiwianRpIjoiNzVlZGM5MGUtMGQwNS00ZWFkLThlNTgtMjQxZjQ4Njk4MDliIiwiY2xpZW50X2lkIjoiY2xpZW50IiwidGVuYW50X2NvZGUiOiJTSEFSUCJ9.O2kDxrbdcr28RH9BAldtfwGgyK3ebQ9UDNOKb5uWYFDF2cNQcQwF3j6NdkgUAwH9-H1tXz8rRKflWsG5xm1X0ya9vUJzNRBP2hpMfXJDQAmiHcSjluC4o0ene84xNrdb8pBuh1-gefl7ykWIQbl5FUmYaThRFwVoLS1t_qvh8rKMqKZ_FXrdLQpdjNE0xeNgEY0vGLA2CaZvdF3B1lMn4g99cQCPxguBZ0fgft1aGuPBZVMdnOMzJaC2D40TZr2srCDhNFtUr0aRLQ9GLDvJB-iPZJWRywMHSw3Hjxwr_U3BXSYHdxsS8d5jhf8Z77Cw0x44wWI9PBObq17HmvalkQ', 'token_type': 'bearer', 'refresh_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3VudHJ5X2NvZGUiOiJKUCIsImxvY2FsZV9jb2RlIjoiZW5fVVMiLCJ1c2VyX25hbWUiOiJhbGV4Iiwic2NvcGUiOlsiZm9vIiwicmVhZCIsIndyaXRlIl0sImF0aSI6Ijc1ZWRjOTBlLTBkMDUtNGVhZC04ZTU4LTI0MWY0ODY5ODA5YiIsImFwcGxpY2F0aW9uX2NvZGUiOiJJREVBUyIsImV4cCI6MTU5NjU0Nzg1NywidXNlcmFjY291bnRfaWQiOiJVQUNfMTAwNDczIiwianRpIjoiYzBiYWM3NjItNzM5Ny00ZmMyLWE2NTItMDNmYjdiNjBkNWE0IiwiY2xpZW50X2lkIjoiY2xpZW50IiwidGVuYW50X2NvZGUiOiJTSEFSUCJ9.VIVmF4oWQv78U1ZpQUaVAfwdCAN3aYn7cCTLCgUn-jVuzprMN62FQnzGPabYNVhchJdXy_2L9Jf5Cz_iVUAvLjGDXKoBM9cA9K_THoNSyPcqsF_fphLsdPf306jfHlsLma1c-N77WwF85XRa-kEETjeuAtyfwul6BZe7HDPNC-sHOs_qFRt2pgYxMThzKNPlZPRByQnvgBJY8dPSbk3-GXUIQcjzAVCqT7_aMbC5bF1pa1MtgMr_VdlRYC8nkEQsyjyvjL_9nY2YO_QzJa_EWzVslMSNfUCF-7JIMfl9HcvH0lLou-z4PE2KxeuWZ8I-PvfW3moL6yYk-cw7-92fdg', 'expires_in': 35999, 'scope': 'foo read write', 'tenant_code': 'SHARP', 'useraccount_id': 'UAC_100473', 'application_code': 'IDEAS', 'locale_code': 'en_US', 'country_code': 'JP', 'jti': '75edc90e-0d05-4ead-8e58-241f4869809b'}
    rep = '"{$.token_type}"=="bearer"'
    result = repl_jsonpth(rep, data)
    print(result)

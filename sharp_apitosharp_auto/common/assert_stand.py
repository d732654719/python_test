import time
def is_valid_date(str):
    '''判断是否是一个有效的日期字符串'''
    if len(str) == 8:
        try:
            time.strptime(str, "%Y%m%d")
            return True
        except:
            return False
    else:
        return False

def is_valid_time(str):
    '''判断是否是一个有效的时间字符串'''
    if len(str) == 6:
        try:
            time.strptime(str, "%H%M%S")
            return True
        except:
            return False
    else:
        return False

def is_valid_shortdate(str):
    '''判断是否是一个有效6位的日期字符串'''
    if len(str) == 6:
        str='20'+str
        try:
            time.strptime(str, "%Y%m%d")
            return True
        except:
            return False
    else:
        return False

def count_after_point(str):
    """ 根据assert_stand里规定的小数位数，判断str是否正确"""

    s = str.split(".")
    count = len(s)
    if count != 2:
        sign = 'm'
    else:
        real_count = 0
        for x in s:
            if x.isdigit():
                real_count += 1
        if real_count == 2:
            sign='p{}'.format(len(s[1]))
        else:
            sign="m"
    return sign

def int_data_sort(str):
    """继续细分整型的字段是日期，还是时间，还是其他"""
    if is_valid_date(str):
        sign = "d"
    elif is_valid_time(str) and is_valid_shortdate(str):
        sign = "c,d"
    elif is_valid_time(str):
        sign = "c"
    elif is_valid_shortdate(str):
        sign = "d"
    else:
        sign = "n"
    return sign
assert_deli = [
    ('m', 'T', 'GK30'),
    ('d', 'T'),
    ('m', 'T'),
    ('m', 'T'),
    ('m', 'T'),
    ('m', 'T'),
    ('m', 'F'),
    ('n', 'T'),
    ('n', 'T', '00'),
    ('n', 'T'),
    ('m', 'T'),
    ('m', 'T'),
    ('m', 'F'),
    ('m', 'F'),
    ('m', 'F'),
    ('n', 'T'),
    ('d', 'T'),
    ('+n', 'T'),
    ('m', 'F'),
    ('+', 'T'),
    ('p2', 'T'),
    ('n', 'T'),
    ('n', 'T'),
    ('n', 'T', '1'),
    ('m', 'F'),
    ('p4', 'T'),
    ('p2', 'T'),
    ('p2', 'T'),
    ('n', 'T'),
    ('m', 'T'),
    ('m', 'T'),
    ('m', 'T'),
    ('m', 'F'),
    ('m', 'F'),
    ('m', 'F'),
    ('m', 'F'),
    ('m', 'F'),
    ('n', 'F'),
    ('m', 'F'),
    ('m', 'F'),
    ('n', 'T'),
    ('n', 'T'),
    ('n', 'T'),
    ('n', 'T'),
    ('m', 'T'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('m', 'T'),
    ('d', 'T'),
    ('m', 'T'),
    ('mn', 'F'),
    ('p2', 'T'),
    ('p2', 'T'),
    ('n', 'T'),
    ('p4', 'T'),
    ('mnd++n', 'T'),
    ('mn', 'T'),
    ('p2', 'T'),
    ('n', 'T'),
    ('p2', 'T'),
    ('n', 'T'),
    ('n', 'T'),
    ('m', 'T'),
    ('d', 'F'),
    ('d', 'T'),
    ('mn', 'F'),
    ('m', 'F'),
    ('m', 'T'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('d', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('mn', 'F'),
    ('n', 'T'),
    ('n', 'T'),
    ('n', 'T'),
    ('n', 'T'),
    ('p2', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('p6', 'T'),
    ('m', 'T'),
    ('p6', 'T'),
    ('m', 'T','GK30'),
    ('mn', 'T'),
    ('d', 'T')

]

assert_sa={
    'SAHD ':[('m', 'T', 'SAHD'),('mn', 'F', ' '), ('n', 'T', '0000'), ('n', 'T', '0000'), ('mnd', 'F', '     '), ('d', 'T'), ('c', 'T'),('n', 'T'),('d', 'F'),('d', 'F'),('m', 'T', "SHARP")],
    'SA021':[('m', 'T', 'SA02'),('mn', 'T', '1'), ('n', 'T'), ('n','T'),('m','F'),('m','F'),('mnd','T'),('m','T'),('m','F'),('n','T'),('n','T'),('d','T'),('n','T'),('m','T'),('m','F'),('m','F')],
    'SA022':[('m', 'T', 'SA02'),('mn', 'T', '2'), ('n', 'T'), ('n','T'),('m','F'),('d','T'),('d','T'),('mnd','T'),('mnd','T'),('m','F'),('mnd','T'),('mnd','T'),('d','T'),('d','T'),('mnd','F'),('mnd','F')],
    'SA023':[('m', 'T', 'SA02'),('mn', 'T', '3'), ('n', 'T'), ('n','T'),('n','T','0000000000000'),('mn','T'),('mn','T'),('m','T'),('n','T'),('m','T'),('n','T'),('m','T'),('n','T'),('mn','T'),('m','T'),('d','T'),('n','T')],
    'SA03 ':[('m', 'T', 'SA03'),('mn', 'F', ' '), ('n', 'T'), ('n','T'),('m','F'),('n','T'),('m','T'),('m','T'),('m','T'),('mn','F'),('m','F'),('n','F'),('mnd','T'),('n','T'),('mnd','F'),('mnd','F'),('n','T'),('n','F'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('mn','T')],
    'SA041':[('m', 'T', 'SA04'),('mn', 'T', '1'), ('n', 'T'), ('n','T'),('mn','T'),('mnd','T'),('mnd','F'),('mnd','T'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T')],
    'SA042':[('m', 'T', 'SA04'),('mn', 'T', '2'), ('n', 'T'), ('n','T'),('nm','F'),('n','T'),('nm','F'),('n','T'),('nm','F'),('n','T'),('nm','F'),('n','T'),('nm','F'),('n','T'),('n','T'),('n','T'),('n','T')],
    'SA05 ':[('m', 'T', 'SA05'),('mn', 'F', ' '), ('n', 'T'), ('n','T'),('m','T'),('mnd','F'),('mnd','F'),('mnd','F'),('mnd','F'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('n','T'),('mnd','F'),('mnd','F')],
    'SA99 ':[('m', 'T', 'SA99'),('mn', 'F', ' '), ('n', 'T','0000'), ('n','T','0000'),('n','T')]
}
if __name__ == '__main__':
    print(is_valid_shortdate('201130'))

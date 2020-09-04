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

if __name__ == '__main__':
    print(count_after_point("000000000000.00"))

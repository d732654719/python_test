import time
def is_valid_date(str):
  '''判断是否是一个有效的日期字符串'''
  try:
    time.strptime(str, "%Y%m%d")
    return True
  except:
    return False



assert_deli = [
    ('m', 'T', 'GK30'),
    ('n', 'T'),
    ('l', 'T'),
    ('l', 'T'),
    ('m', 'T' ),
    ('m', 'T'),

]
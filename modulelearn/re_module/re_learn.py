import re

# a = "a;d\nde"
# b = re.split("[;\n]",a)
# print(b)
# s='abc,  abc,  defg,  dds'
# sp = re.split('[,a]',s)
# print(sp)
rep = '{"username":"{$..ids[0][0]}","password":"{$..pwd[0][0]}","clientId":"visual"}'
a = re.search("{(\$.*?)}", rep)
print(a)
print(a.groups())
print(a.group(1))

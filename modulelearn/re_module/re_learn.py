import re
a = "a;d\nde"
b = re.split("[;\n]",a)
print(b)
s='abc,  abc,  defg,  dds'
sp = re.split('[,a]',s)
print(sp)

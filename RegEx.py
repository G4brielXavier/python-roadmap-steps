import re

msg ='''

Gabriel
Xavier
@dasd
Suzana
Junior
2983Calor

'''

pattern = re.compile('[\w]')

x = re.findall(pattern, msg)    

print(x)
import re
t=re.search(r'FishC','I love FishC.com')
print(t)
t=re.search(r'.','I love FishC.com')
print(t)
s=re.search(r'ab{3,10}c','abbbbbbbbc')
print(s)
r=re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.209.155')
print(r)
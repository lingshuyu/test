
num={}
print(type(num))
num1={1,2,3,4,5,6}
print(type(num1))
num2={1,3,4,5,6,4,2,3,1,4,5}
print(num2)
num3=[1,2,3,4,5,6,4,3,7]
temp=[]
for each in num3:
    if each not in temp:
        temp.append(each)
print(temp)

f=open('D:\\lin.txt',encoding='utf-8')
print(f.read())
print(f.tell())
print(f.seek(0,1))
'''
for each_line in f:
    print(each_line)
'''
d=open('D:\\text.txt','w',encoding='utf-8')
d.write('I love tcl')
print(d)

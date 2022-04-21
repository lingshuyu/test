
f=open('D:\\lin.txt',encoding='utf-8')
print(f.read())
boy=[]
girl=[]
count=1
for each_line in f:
    if each_line[:6] != '------':
        (role,line_spoken)=each_line.split('、',1)
        if role =='百度快照':
            boy.append(line_spoken)
        if role =='湖南':
            girl.append(line_spoken)
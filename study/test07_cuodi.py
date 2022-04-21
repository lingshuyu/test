file_name=input('请输入需要打开的文件名：')
f=open(file_name,encoding='utf-8')
print('文件的内容：')
for each_line in f:
    print(each_line)
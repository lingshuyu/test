import  pickle
my_list=[123,3.14,'唐和林',['another list']]
pickle_file = open('my_list.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle_file.close()
pickle_file=open('my_list.pkl','rb')
my_list2=pickle.load(pickle_file)
print(my_list2)

city={'海口':'101301403'}
import urllib.request
import json
password=input('请输入城市：')
name1=city[password]
File1=urllib.request.urlopen('http://m.weather.com.cn/data/'+name1)

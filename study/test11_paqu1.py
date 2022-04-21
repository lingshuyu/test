import urllib.request
import urllib.parse
import json
content=input('请输入需要翻译的内容')
url='https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data={}
data['from']='AUTO'
data['to']='AUTO'
data['i']=content
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='16224702539347'
data['sign']='97d3108b016113cd1167f5064997d7ff'
data['lts']='1622470253934'
data['bv']='9ff8102373b1562471f4b6881a5653e9'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_REALTlME'
data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

json.loads(html)
target = json.loads(html)
t=target['translateResult'][0][0]['tgt']
print('翻译结果：%s' % (t))
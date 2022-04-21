'''
favourite = 'fishc'
for i in favourite:
    print(i,end=' ')

member=['林','唐','汪']
for each in member:
    print(each,len(each))


for i in range(5):
    print(i)

print('----------')
for i in range(3,10,3):
    print(i)

print('----------')

bingo = 'tcl'
answer = input('请输入:')
while True:
    if answer == bingo:
        break
    answer = input('抱歉哦，请重新输入：')
print('bingo,答对了。')

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i+=2
    print(i)
'''

member=['林','唐','汪']
member.extend(['范','刘'])
member.insert(0,'窦')
print(member)
member.reverse()
print(member)

print('--------')
list1=[123]
list2=[456]
if list1>list2:
    print('list1>list2')
else:
    print('list1<list2')

list3=[2,4,6,5,3,1]
list3.sort(reverse=0)
print(list3)

tuple1=(1,4,2,3,7,8,5,3,9)
print(tuple1[2:5])
print(type(tuple1))
a=8*(8)
b=8*(8,)
print(a)
print(b)
tuple1=tuple1[:5]+(10,)+tuple1[5:]
print(tuple1)
str1='xiaoxie'
print(str1.capitalize())

print(str1.center(50))
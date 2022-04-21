'''s={1,3,4,5,7,8,9}


for i in s:
    print(i)

for index,i in enumerate(s):
    print(index,i)

print(enumerate(s))

list1=[]
index=0
for i in s:
    t1=(index,i)
    list1.append(t1)

    index+=1

print(list1)

for index,value in list1:
    print(index,value)
'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = list1
list1.remove(5)
print(list2)

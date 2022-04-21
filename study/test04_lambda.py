def ds(x):
    return 2*x +1
print(ds(5))

lambda x : 2*x+1
g=lambda x : 2*x+1
print(g(5))
lambda x,y : x+y
b = lambda x,y : x+y
print(b(3,4))
filter(None,[1,0,False,True])
a=list(filter(None,[1,0,False,True]))
print(a)
def odd(x):
    return x%2
temp = range((10))
show=filter(odd,temp)
c=list(show)
print(c)

d=list(filter(lambda x : x%2,range(10)))
print(d)

e=list(map(lambda x :x*2,range(10)))
print(e)
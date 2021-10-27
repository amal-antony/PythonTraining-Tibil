#len
my_tuple=(1, 2, 3, [6, 5])
l=len(my_tuple)
print(l)

#max
a=(3,1,2,5,4,6)
m=max(a)
print(m)

#min
n=min(a)
print(n)

#sum
s=sum(a)
print(s)

#sorted
x=sorted(a)
print(x)

#index
a=(1,2,3,2,4,5,2)
search=a.index(2)
print(search)

#count
result=print(a.count(2))

#membership-in
'a' in tuple("string")

#concatentaion
newtup=(1,2,3)+(4,5,6)
print(newtup)

#identity
a=(1,2)
b=(1,2)
print(b is a)
n= int(input())
t=[]

for i in range(n):
    x=int(input())
    t.append(x)
tup=tuple(t)
print(tup)
print(hash(tup))
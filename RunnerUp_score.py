n= int(input())
array=[]
for i in range (n):
    item=int(input())
    array.append(item)
new_array=set(array)
new_array.remove(max(new_array))
print(max(new_array))
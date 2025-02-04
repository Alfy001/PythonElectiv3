master=[1,4,5,6,3,8,9,2]
min=[]
q=int(input("enter  the number u want"))
for i in master:
    if i<q:
        min.append(i)
    else:
        continue
print(min)

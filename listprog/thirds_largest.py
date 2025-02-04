a=[9,3,8,1,6,7,4,2]
d=int(input("entr the postion to find the greatest number"))
for i in range(d-1):
    s=max(a)
    a.remove(s)
    
print("the third largest number is :=",max(a))

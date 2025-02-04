n = int(input("Enter number of elements : "))
list_1 = [int(input()) for i in range(0, n)]
print("List: ",list_1)

m = int(input("Enter number of elements : "))
list_2= [int(input()) for i in range(0, n)]
print("List: ",list_2)

list_3=[i for i in list_1 if i in list_2]
print(list_3)

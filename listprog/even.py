h = [1,2,3,4,5,6,7,8,9,0]

even = [i for i in h if i % 2 == 0]

even.sort()
print("original")
print(h)
print("\n")
print("the list of even number")
print(even)
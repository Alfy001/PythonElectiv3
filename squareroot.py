num = float(input("Enter the number: "))

if num < 0:
    print("Square root of negative number is complex:", complex(0, (-num) ** 0.5))
else:
    sqrroot = num ** 0.5
    print("Square Root:", sqrroot)

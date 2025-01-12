p = float(input("Enter amount: "))
r = float(input("Enter rate: ")) / 100
t = int(input("Enter years: "))
n = int(input("Enter compounding times: "))

final = p * (1 + r / n) ** (n * t)
print("Final Amount:", final)

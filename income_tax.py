def calculate_tax(income):
    tax = 0
    surcharge = 0
    
    if income <= 300000:
        tax = 0
        surcharge = 0
    elif income <= 700000:
        tax = (income - 300000) * 0.05
        surcharge = 0
    elif income <= 1000000:
        tax = 20000 + (income - 700000) * 0.1
        surcharge = 0
    elif income <= 1200000:
        tax = 50000 + (income - 1000000) * 0.15
        surcharge = 0
    elif income <= 1500000:
        tax = 80000 + (income - 1200000) * 0.2
        surcharge = 0
    elif income <= 5000000:
        tax = 140000 + (income - 1500000) * 0.3
        surcharge = 0
    elif income <= 10000000:
        tax = 140000 + (income - 1500000) * 0.3
        surcharge = 0.1 * tax
    elif income <= 20000000:
        tax = 140000 + (income - 1500000) * 0.3
        surcharge = 0.15 * tax
    else:
        tax = 140000 + (income - 1500000) * 0.3
        surcharge = 0.25 * tax

    total_tax = tax + surcharge
    return total_tax

income = float(input("Enter your income: ₹"))
tax = calculate_tax(income)
print(f"Your total income tax is: ₹{tax:.2f}")
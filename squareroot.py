num_input = int(input("Enter a number: "))
approx_root = 1

if num_input < 0:
    print("Square root of a negative number is not a real number.")
else:
    for i in range(num_input):
        if num_input == (approx_root * approx_root):
            break
        approx_root += 1
    approx_root = (approx_root + num_input / approx_root) / 2
    error = abs(num_input - approx_root ** 2)

    if error == 0:
        print("The Square root 0f", num_input, "=", approx_root)

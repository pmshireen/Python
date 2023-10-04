def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num_str = input("Enter a number: ")
num = int(num_str)  # Convert the input to an integer
print("Factorial of", num, "is", factorial(num))

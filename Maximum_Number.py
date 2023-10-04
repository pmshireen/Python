def maximum(a , b):
    if a >= b:
        return a
    else:
        return b
    
num1 = input("Enter a number n1 ")
num2 = input("Enter a number n2 ")
# print(maximum(num1,num2))

# Using max of function
maxElement = max(num1, num2)
print(maxElement)
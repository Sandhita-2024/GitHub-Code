def factorial(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result
num = int(input("Enter the number: "))

if num <0 :
    print("The factorial is not define for the negative numbers. ")
else:
    print("The factorial of the", num, "is", factorial(num))
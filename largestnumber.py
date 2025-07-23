numbers = input("Enter numbers separated by spaces: ")

numbers_list = [float(num) for num in numbers.split()]

largest = max(numbers_list)

print("The Largest Number is: ", largest)

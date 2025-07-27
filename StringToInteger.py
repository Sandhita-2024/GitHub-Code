def convert_to_integer(string_number):
    try:
        return int(string_number)
    except ValueError:
        return "Invalid input! Please enter a numeric string."

input_str = input("Enter a number as a string: ")
result = convert_to_integer(input_str)
print("Converted integer:",result)
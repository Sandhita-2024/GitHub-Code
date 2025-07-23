def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
            
    return count

user_input = input("Enter the word: ")

vowels_count = count_vowels(user_input)
print("Number of vowels are: ", vowels_count)
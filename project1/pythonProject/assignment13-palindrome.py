# Check if a string is a palindrome

user_input = input("Enter a string: ")

# Remove spaces and convert the string to lowercase
s = user_input.replace(" ", "").lower()

# Initialize a flag to indicate if it's a palindrome


# Loop structure to compare characters from both ends
for letter in range(len(s) // 2):
    if s[letter] != s[len(s) - 1 - letter]:
        is_palindrome = False  # If characters don't match, it's not a palindrome
        break  # No need to continue checking if we found a mismatch

# Output the result
if is_palindrome:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
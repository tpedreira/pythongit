# Check if a string is a palindrome


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

palindrome = input("Enter a string: ")
if is_palindrome(palindrome):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

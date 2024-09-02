# Check if a string is a palindrome


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

palindrome = input("Enter a string: ")
if is_palindrome(palindrome):
    print("True, the string is a palindrome.")
else:
    print("False, the string is not a palindrome.")


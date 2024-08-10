# Determine if a character is a vowel or consonant
# This one took me a little bit to figure out how to get the program to go back to the Enter a letter but I finally got it!
# Im actually proud to have done it all on my own. The only things I needed to research was the .isalpha method
def letterCheck():
    letter = str(input("Enter a letter to determine if it is a Vowel or Consonant: ")).upper()
    if letter == "A":
        print("The letter A is a vowel")
    elif letter == "E":
        print("The letter E is a vowel")
    elif letter == "I":
        print("The letter I is a vowel")
    elif letter == "O":
        print("The letter O is a vowel")
    elif letter == "U":
        print("The letter U is a vowel")
    elif:
        print("The letter " + letter + " is a consonant")
    else: letter != letter.isalpha():
        print("Please enter a letter")
        letterCheck()

letterCheck()



#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#Note: Pangrams are words or sentences containing every letter of the alphabet at least once. For example: "The quick brown fox jumps over the lazy dog"

def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if char not in str.lower():
            return "Not a pangram"
        
    return "It is a pangram"
        
str = input("Enter a sentence to check whether it is pangram:")
result = pangram(str)
print(result)

#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"


#create a function to input parameters
def palindrome(text):

    length = len(text)

    #Divide the length of the word in two, compare first index to last index in the other half  of the length 
    for i in range(0, length // 2):
        #Increment index in first half and and decrement last index in the other half and compare.
        if (text[i] != text[length - i - 1] ):
            return "Not a palindrome"
        else:
            return "It is a palindrome"

text = input("Enter a word to check if it is a palindrome:")
result = palindrome(text)
print(result)
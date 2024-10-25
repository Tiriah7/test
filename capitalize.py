#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.
def capitalize(str):
    return ' '.join(word.title() for word in str.split())

str = input("Enter the sentence:")
result = capitalize(str)
print(result)
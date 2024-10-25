#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse(n):
        # Check if the number is negative
    if n < 0:
        # Reverse the string of digits, excluding the negative sign, and restore the negative sign
        return -int(str(n)[:0:-1])
    else:
        # Reverse the string of digits and convert it back to an integer
        return int(str(n)[::-1])

n = int(input("Enter number:"))
result = reverse(n)
print(result)

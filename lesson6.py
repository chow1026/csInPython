# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    out = 1
    while n > 1:
        out *= n
        n -= 1
    return out

### CORRECT ANSWER ###
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))
#>>> 1
print(factorial(5))
#>>> 120
print(factorial(10))
#>>> 3628800




# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if len(s) > 1:
        i = 0
        while i < len(s)//2:
            # print(s[i])
            # print(s[-(i + 1)])
            if s[i] != s[-(i + 1)]:
                return False
            i += 1
    return True

### CORRECT ANSWER ###
def is_palindrome(s):
    if s == "":
        return True
    else:
        if s[0] == s[1]:
            return is_palindrom(s[1:-1])
        else:
            return False

print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
print is_palindrome('abeba')
#>>> True
print is_palindrome('andrea')

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

def is_palindrome(s):
    for i in range(0, len(s) /2):
        if s[i] != s[-(i + 1)]:
            return False
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



# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci (n-1) + fibonacci(n-2)

print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610

36 -> 1
35 -> 1
34 -> 2
33 -> 3
32 -> 5
31 -> 8
30 -> 13

0 50000
1 50000 + 50000 * 2 = 150000
2


#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n <= 1:
        return n

    last_two = [0, 1]
    i = 1
    while i < n:
        last_two.append(last_two[0] + last_two[1])
        last_two.pop(0)
        i += 1
    return last_two[1]

### ANSWER ###
def fibonacci(n):
    current = 0
    after = 1
    for i in range (0, n):
        current, after = after, current + after
    return current

print fibonacci(36)
#>>> 14930352


mass_of_earth = 5.9722 * 10**24 #kilogram
mass_of_rabbit = 2

n = 1
while fibonacci(n) * mass_of_rabbit < mass_of_earth:
    n = n + 1
print(n)

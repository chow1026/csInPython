###################################################
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter
# print udacify('dacians')
# the output should be the string 'Udacians'
###################################################
def udacify(suffix):
    if isinstance(suffix, str):
        return "U" + suffix
    else:
        return "Invalid input."

# Remove the hash, #, from infront of print to test your code.

print(udacify('dacians'))
#>>> Udacians

print(udacify('turn'))
#>>> Uturn

print(udacify('boat'))
#>>> Uboat



###################################################
# See if which among proc1, proc2, proc3 and proc4
# does the same as proc procedure
###################################################
def proc(a,b):
    if test(a):
        return b
    return a

# same
def proc1(x, y):
    if test(x):
        return y
    else:
        return x

# not same
def proc2(a,b):
    if not test(b):
        return a
    else:
        return b

# same
def proc3(a,b):
    result = a
    if test(a):
        result = b
    return result

# same
def proc4(a,b):
    if not test(a):
        b = 'udacity'
    else:
        return b
    return a



###################################################
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.
# Make sure your procedure has a return statement.
###################################################
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    if (a == biggest(a, b, c)):
        return bigger(b, c)
    elif (b == biggest(a, b, c)):
        return bigger(a, c)
    else:
        return bigger(a, b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))


###################################################
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).
###################################################
def countdown(n):
    if isinstance(n, int):

        while (n >= 0):
            print n
            n -= 1
            if (n == 0):
                print "Blastoff!"
                break
    else:
        print("Invalid entry.")


countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!




###################################################
# For each of the loops below determine whether
# the loop always finishes no matter what positive
# integer value is assigned initially to n.
###################################################

# Loop 1 - always finishes
def loop1(n):
    n > 0
    i = 0
    while i <= n:
        i = i + 1

# Loop 2 - always finishes
def loop2(n):
    n > 0
    i = 1
    while True:
        i = i * 2
        n = n + 1
        if i > n:
            break

# Loop 3 - unknown.
def loop3(n):
    n > 0
    while n != 1:
        if n % 2 == 0: #n is even
            n = n/2
        else:
            n = 3 * n + 1



###################################################
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
# Example: find_last('aaaa', 'a') returns 3
# Make sure your procedure has a return statement.
###################################################

def find_last(search, target):
    index = search.find(target)
    while (index + len(target) < len(search)):
        if (search.find(target, index + 1) > index):
            index = search.find(target, index + 1)
            #print("reindex - " + str(index))
        else:
            break
    return index

print(find_last('aaaa', 'a'))
#>>> 3

print(find_last('aaaaa', 'aa'))
#>>> 3

print(find_last('aaaa', 'b'))
#>>> -1

print(find_last("111111111", "1"))
#>>> 8

print(find_last("222222222", ""))
#>>> 9

print(find_last("", "3"))
#>>> -1

print(find_last("", ""))
#>>> 0

print(find_last("abbaabbabbbaaaabbba", "ab"))

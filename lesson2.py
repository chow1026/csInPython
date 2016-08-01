###################################################
# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.
###################################################
def sum(a,b):
    c = a + b
    return c

def square(n):
    if isinstance(n, int) or isinstance(n, float):
        return n*n
    else:
        return "Error!"

# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure.

print square(5)
#>>> 25


###################################################
# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.
###################################################
def sum(a,b):
    return a + b

def sum3(a, b, c):
    return a + b + c

print sum3(1,2,3)
#>>> 6

print sum3(93,53,70)
#>>> 216


###################################################
# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.
###################################################
def abbaize(m, n):
    return m + n + n + m

print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'


###################################################
# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.
###################################################
def find_second(search_str, target_str):
    first_index = search_str.find(target_str)
    return search_str.find(target_str, first_index + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13


###################################################
# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.
###################################################
def bigger(a, b):
    if (isinstance(a, float) or isinstance(a, int)) and (isinstance(a, float) or isinstance(a, int)):
        if (a > b):
            return a
        elif (b > a):
            return b
        elif (a == b):
            return b
        else:
            return "Error comparing two inputs."
    else:
        return "One or more inputs are not numeric."

print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3


###################################################
# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'
###################################################
def is_friend(name):
    if isinstance(name, str):
        if (name[0] == "D") or (name[0] =="d"):
            return True
        else:
            return False
    else:
        return "Invalid name."

print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False


###################################################
# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'
###################################################
def is_friend(name):
    if isinstance(name, str):
        if (name[0] == "D") or (name[0] == "d") or (name[0] == "N") or (name[0] == "n"):
            return True
        else:
            return False
    else:
        return "Invalid name."

print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False


###################################################
# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.
###################################################
def biggest(a, b, c):
    if (isinstance(a, float) or isinstance(a, int)) \
    and (isinstance(b, float) or isinstance(b, int)) \
    and (isinstance(c, float) or isinstance(c, int)):
        return max([a, b, c])
    else:
        return "Invalid inputs."

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9


###################################################
# Define a different biggest procedure, biggest2, that takes three
# numbers as inputs and returns the largest of
# those three numbers.
###################################################
def biggest2(a, b, c):
    if (isinstance(a, float) or isinstance(a, int)) \
    and (isinstance(b, float) or isinstance(b, int)) \
    and (isinstance(c, float) or isinstance(c, int)):
        # return max([a, b, c])
        if a > b:
            if a > c:
                return a
            else:
                return c
        else:
            if b > c:
                return b
            else:
                return c
    else:
        return "Invalid inputs."

print(biggest2(3, 6, 9))
#>>> 9

print(biggest2(6, 9, 3))
#>>> 9

print(biggest(9, 3, 6))
#>>> 9

print(biggest(3, 3, 9))
#>>> 9

print(biggest(9, 3, 9))
#>>> 9


###################################################
# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.
###################################################
# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    if (n > 0) and isinstance(n, int):
        i = 0
        while (i < n):
            i += 1
            print(i)
    else:
        print("{0} is not a positive integer.".format(n))

print_numbers('a')
#>>> a is not a positive integer.
print_numbers(3)
#>>> 1
#>>> 2
#>>> 3


###################################################
# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.
###################################################
def factorial(n):
    if isinstance(n, int) and (n >= 0):
        factorial = 1
        if n == 0:
            return factorial
        else:
            while (n > 0):
                factorial *= n
                n -= 1
            return factorial
    else:
        return "Invalid input."


print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

###################################################
# Define procedures, testwhile & testbreak, to
# test different ways of code to achieve the same
# output.
###################################################
def testwhile(countdown):
    while countdown >= 0:
        print(countdown)
        countdown = countdown - 1

testwhile(10)

def testbreak(countdown):
    while True:
        if countdown < 0:
            break
        print(countdown)
        countdown = countdown - 1

testbreak(10)



###################################################
# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.
###################################################
# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.
#page = '''<div id="top_bin"> <div id="top_content" class="width960">
#   <div class="udacity float-left"> <a href="/">'''

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> Hot "butt" </div></div>'''

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if (start_link < 0):
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

get_next_target(page)

###################################################
# alternative to the above get_next_target
###################################################
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> Hot "butt" </div></div>'''

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if (start_link < 0):
        return None, 0
    # note that no else needed.  
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

get_next_target2(page)



###################################################
# Write a print_all_links procedure so that
# it prints out all links from a page
###################################################
def print_all_links(page):
    while true:
        url, endpost = get_next_target(page)
        if url:
            print(url)
            page = page[endpost:]
        else:
            break



###################################################
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter
###################################################
# print udacify('dacians')

# the output should be the string 'Udacians'

def udacify(suffix):
    if isinstance(suffix, str):
        return "U" + suffix
    else:
        return "Invalid input."

# Remove the hash, #, from infront of print to test your code.

print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat


###################################################
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.
###################################################
# Make sure your procedure has a return statement.
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
#>>> 7


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
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.
###################################################
def weekend(day):
    # your code here
    weekend = False
    if (day == 'Saturday') or (day == 'Sunday'):
        return True
    else:
        return False


print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False


###################################################
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
###################################################

def stamps(n):
    # Your code here
    p5 = n // 5
    p2 = (n % 5) // 2
    p1 = (n % 5) % 2

    return p5, p2, p1


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps


###################################################
# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.
###################################################
# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a, b, c):
    # Your code here
    big = max(a, b, c)
    small = min(a, b, c)
    return (big - small)


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6


###################################################
# By Websten from forums
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
# Assume that the birthday and current date are correct dates (and no time travel).
###################################################
from datetime import date

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)
    td = date2 - date1
    return td.days

# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()



#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
       #
       ### Add you code here
       #
       l = len(str(value))
       i = 0
       while (i < 10):
           if (i == 10 - l):
               j = 0
               while (j < l):
                   print("str(value)[j]")

           print("|00000*****   |")
           i += 0


###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

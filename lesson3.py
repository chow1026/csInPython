
def sum_list(ls):
    i = 0
    sum = 0
    while (i < len(ls)):
        sum += ls[i]
        i += 1
    return sum

print(sum_list([1, 7, 4]))
#>>> 12

print(sum_list([9, 4, 10]))
#>>> 23

print(sum_list([44, 14, 76]))
#>>> 134

def measure_udacity(ls):
    count = 0
    for char in ls:
        if (char[0] == "U"):
            count += 1
    return count

print(measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print(measure_udacity(['Umika','Umberto']))
#>>> 2

def find_element0(ls, find):
    i = 0
    while i < len(ls):
        if ls[i] == find:
            return i
        else:
            return -1


def find_element1(ls, find):
    if find in ls:
        return ls.index(find)
    else:
        return -1

print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))
#>>> -1

def union(ls1, ls2):
    for x in ls2:
        if not (x in ls1):
            ls1.append(x)

a = [1,2,3]
b = [2,4,6]
union(a,b)
print(a)
#>>> [1,2,3,4,6]
print(b)
#>>> [2,4,6]


# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

def list_mean(lst):

    if lst:
        sum = 0
        for n in lst:
            sum += n
        return float(sum)/len(lst)
    else:
        return float(0)



print(list_mean([1,2,3,4]))
#>>> 2.5
print(list_mean([1,3,4,5,2]))
#>>> 3.0
print(list_mean([]))
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print(list_mean([2]))
#>>> 2.0




# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    # YOUR CODE
    i = 1
    lst = [int(string[0])]
    bg = int(string[0]) # first number as preceding y
    sblst = []
    while i < len(string):
        # print("=== BEFORE ===")
        # print("x", string[i])
        # print("lst", lst)
        # print("sblst", sblst)
        # print("bg", bg)

        if int(string[i]) > int(string[i - 1]):
            if int(string[i]) > bg:
                if len(sblst) > 0:
                    lst.append(sblst)
                    sblst = []
                bg = int(string[i])
                lst.append(int(string[i]))
            else:
                sblst.append(int(string[i]))
        else:
            sblst.append(int(string[i]))

        # if x is last number,
        if i == (len(string)-1) and len(sblst) > 0:
            lst.append(sblst)
            sblst = []

        # print("=== AFTER ===")
        # print("lst", lst)
        # print("sblst", sblst)
        # print("bg", bg)
        i += 1
    print(lst)
    return lst

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print(result)
print(repr(string), numbers_in_lists(string) == result)
print("===+++ END +++===")
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print(result)
print(repr(string), numbers_in_lists(string) == result)
print("===+++ END +++===")
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print(result)
print(repr(string), numbers_in_lists(string) == result)
print("===+++ END +++===")
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(result)
print(repr(string), numbers_in_lists(string) == result)
print("===+++ END +++===")


# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains
# the lowercase letters a-z.
# As output you should return a list of the normalized frequency
# for each of the letters a-z.
# The normalized frequency is simply the number of occurrences, i,
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    ##
    # Your code here
    ##
    freq_list = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in alpha:
        freq_list.append(float(message.count(char))/float(len(message)))
    print(len(message))
    return freq_list

#Tests
print(freq_analysis("abcd"))
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis("adca"))
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis('bewarethebunnies'))
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

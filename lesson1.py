# Lesson 1 Exercise

####################################################
# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.
####################################################
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a href=')
print(start_link)


####################################################
# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.
####################################################
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a href=')
print(start_link)


####################################################
# Write Python code that prints out the number of
# hours in 7 weeks.
####################################################
weeks = 7
days = weeks * 7
hours = days * 24
print(hours)


####################################################
# Write Python code that stores the distance
# in meters that light travels in one
# nanosecond in the variable, nanodistance.
####################################################
# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

# After your code, running the following:
# print nanodistance
# should output: 0.2998
# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line
nanodistance = (1.0 / nano_per_sec) * speed_of_light
print nanodistance


####################################################
# String Manipulation
####################################################
# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
o = s[0] + t[2:]
print(o)


####################################################
# Assume text is a variable that holds a string. Write Python code
# that prints out the position of the first occurrence of 'hoo'
# in the value of text, or -1 if it does not occur at all.
####################################################
text = "first hoo"
print(text.find('hoo'))


####################################################
# Assume text is a variable that holds a string. Write Python code
# that prints out the position of the second occurrence of 'zip'
# in text, or -1 if it does not occur at least twice.
####################################################
# The Python code should be general enough to pass every
# possible case where 'zip'  can occur in a string
# Here are two example test cases:
# text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"
print(text.find('zip', text.find('zip') + 3))
# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function


####################################################
# Given a variable, x, that stores the value of any
# decimal number, write Python code that prints out the
# nearest whole number to x.
# If x is exactly half way between two whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.
####################################################

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved
# using just the information introduced in unit 1.

# x = 3.14159
# >>> 3 (not 3.0)
# x = 27.63
# >>> 28 (not 28.0)
# x = 3.5
# >>> 4 (not 4.0)

# String Manipulation Method
x = 3.14159
x += 0.5
print(str(x)[:str(x).find('.')])
x = 27.63
x += 0.5
print(str(x)[:str(x).find('.')])
x = 3.5
x += 0.5
print(str(x)[:str(x).find('.')])
x = 6.349838
x += 0.5
print(str(x)[:str(x).find('.')])

# Math Rounding up Method
x = 3.14159
print(int(round(x)))
x = 27.63
print(int(round(x)))
x = 3.5
print(int(round(x)))
x = 6.349838
print(int(round(x)))


####################################################
# Given a string s = "CidatyUcityda", which of the
# following expressions is equivalent to the string
# "Udacity"? (Note that none of the choices actually
# print out anything, so a strictly correct answer to
# this would be none of them.
# But, the intent of the question is to select answers that
# evaluate to the string.)
####################################################
s = 'CidatyUcityda'
u = s.find('U')
da = s.find('da')
city = s.find('city')

print(s[6] + s[-2:] + s[7:11])
print(s[6] + s[2] + s[3] + s[7:11])
print(s[-7] + s[2:4] + s[7:11])


###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace
# the tricky parts with a marker.
# Write a program that takes a line of text and
# finds the first occurrence of a certain marker
# and replaces it with a replacement text.
# The resulting line of text should be stored in a variable.
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# Hint: You can find out the length of a string by command
# len(string). We might test your code with different markers!

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."
replaced = line.replace(marker, replacement)
print replaced

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."
replaced = line.replace(marker, replacement)
print replaced

###
# YOUR CODE BELOW. DO NOT DELETE THIS LINE
###
abbrev = "AFAIK"
full = "as far as I know"
sentense = "Angela has not commited any felony AFAIK."
replaced = sentense.replace(abbrev, full)
print replaced
# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.


##################################################################
#      Arithmatic Differences Between Python 2 and Python 3      #
##################################################################

# Python 2.7.11
print 10/4.0
# >>> 2.5
print 10/4
# >>> 2
print 10.0/5
# >>> 2.0
print 10*1.0/4
# >>> 2.5
print 10/5
# >>> 2
print 10/50
# >>> 0

# Python 3.5.1
print(10/4.0)
# >>> 2.5
print(10/4)
# >>> 2.5
print(10.0/5)
# >>> 2.0
print(10*1.0/4)
# >>> 2.5
print(10/2)
# >>> 5.0
print(10/50)
# >>> 0.2


###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads
# the same backwards as forwards. Make a program
# that checks if a word is a palindrome.
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise.
# The word contains lowercase letters a-z and
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
# test case 2
# word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###

is_palindrome = 0 if bool(word == word[::-1]) else -1

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"

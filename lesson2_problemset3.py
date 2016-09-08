###############################################################################
# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: #
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #
###############################################################################


def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    i = 0
    while (i < len(product)):
        index = debris.find(product[i])
        i += 1
        if (index < 0):
            return "Give me something that's not useless next time."

    return product

### TEST CASES ###
print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print ("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print ("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print ("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')




#############################################################################
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
##############################################################################
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




##############################################################################
# By AnnaGajdova from forums
# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.
##############################################################################
def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    cheetah_speed = 115
    if (animal == 'cheetah'):
        print "Run!" if (my_speed > 115) else "Stay calm and wait!"
    elif (animal == 'zebra'):
        print "Try to ride a zebra!"
    else:
        print "Introduce yourself!"


jungle_animal('zebra', 130)

jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"




##############################################################################
# By Ashwath from forums
# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.
# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).
##############################################################################
def is_leap_baby(day,month,year):
    # Write your code after this line.
    if ((day == 29) and (month == 2)):
        if (year % 400 == 0):
            return True
        elif (year % 4 == 0):
            return True if (year % 100 <> 0) else False
        else:
            return False
    else:
        return False

# The function 'output' prints one of two statements based on whether
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!" % name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!" % name

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(19, 6, 1978), 'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29, 2, 2000), 'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28, 2, 1976), 'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!

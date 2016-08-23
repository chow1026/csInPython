# The following will leave the values passed in as the input unchanged.

# False #
def proc1(p):
    p[0] = p[1]

# True #
def proc2(p):
    p = p + [1]

# True #
def proc3(p):
    q = p
    p.append(3)
    q.pop()

# True #
def proc4(p):
    q = []
    while p:
        q.append(p.pop())
    while q:
        p.append(q.pop())

# Write a product_list procedure to return the number that is the result of multiplying the numbers from the list passed in
def product_list(list_of_numbers):
    prod = 1
    print("len = " + str(len(list_of_numbers)))
    if len(list_of_numbers) == 0:
        return prod
    else:
        for num in list_of_numbers:
            prod = prod * num
        return prod

print(product_list([9]))
#>>> 9

print(product_list([1,2,3,4]))
#>>> 24

print(product_list([]))
#>>> 1

# Define a procedure, greatest, that takes as input a list of positive numbers, and returns the greatest number in that list. If the input list is empty, the output should be 0.

def greatest0(list_of_numbers):
    if len(list_of_numbers) > 0:
        return max(list_of_numbers)
    else:
        return 0

def greatest(list_of_numbers):
    bg = 0
    for num in list_of_numbers:
        if num > bg: bg = num
    return bg

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

# Define a procedure, total_enrollment, that takes as an input a list of elements, where each element is a list containing three elements: a university name, the total number of students enrolled, and the annual tuition fees.

# The procedure should return two numbers, not a string,  giving the total number of students enrolled at all of the universities in the list, and the total tuition fees (which is the sum of the number of students enrolled times the tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(univs):
    tot_students = 0
    tot_tuition = 0
    # univs = usa_univs.append(udacious_univs)
    # print(len(univs))
    for univ in univs:
        tot_students += univ[1]
        tot_tuition += univ[1] * univ[2]
    return tot_students, tot_tuition

print(total_enrollment(udacious_univs))
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside
# interpreter you might not see it.

print(total_enrollment(usa_univs))
#>>> (77285,3058581079)

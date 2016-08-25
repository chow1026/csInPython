import time

def time_execution(code):
    start = time.clock()
    result = eval(code) #run the code
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

time_execution('lookup(index10000, "udacity")')
# >>>(None, 0.000968000000000302)

time_execution('lookup(index10000, "udacity")')
# >>>(None, 0.000905999999863066)

time_execution('lookup(index100000, "udacity")')
# >>>(None, 0.008590000000002652)

time_execution('lookup(index100000, "udacity")')
# >>>(None, 0.008517999999998093)

print(time_execution('spin_loop(10**9)'))

def make_big_index(size):
    index = []
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                  letters[i] = chr(ord(letters[i]) + 1)
                  break
            else:
                   letters[i] = 'a'
    return index

def make_big_index(size):
    index[]
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, "fake")
        for i in range(len(letters) -1, 0 , -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letter[i] + 1))
                break
            else:
                letters[i] = 'a'
    return index

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

indx100000 = make_big_index(100000)

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results



def bad_hash_string(keyword, buckets):
    return ord(keyword[0])%buckets

# bad because it produce error if keyword is "" [empty string]
# bad because if the keywords are distributed like words in English, some buckets will get too many words
# bad because if the number of buckets is large, some buckets will not get any keywords.


# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in
# the correct bucket), with the correct
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable,key,value):
    # your code here
    htable[hash_string(key,len(htable))].append([key, value])
    return htable

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]



# Define a procedure,
# hashtable_lookup(htable,key)
# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

def hashtable_lookup(htable,key):
    ##### BETTER CODE #####
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None
    ##### MY CODE #####
    for bucket in htable:
        for keypair in bucket:
            if keypair[0] == key:
                return keypair[1]
    return None

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
print hashtable_lookup(table, 'Francis')
#>>> 13
print hashtable_lookup(table, 'Louis')
#>>> 29
print hashtable_lookup(table, 'Zoe')
#>>> 14


# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable

def hashtable_update(htable,key,value):
    ##### BETTER CODE #####
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] == value
            return
    bucket.append([key,value])
    ##### MY CODE #####
    done = False
    for bucket in htable:
        for keypair in bucket:
            if keypair[0] == key:
                keypair[1] = value
                done = True
                break
    if not done:
        hashtable_add(htable,key,value)
    return htable

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]



# Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],['Zoe', 14]], [['Coach', 4]], [['Louis', 29],['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]
print hashtable_get_bucket(table, "Brick")
#>>> []
print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]



# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.
def hash_string(keyword,buckets):
    sum_hash = 0
    for char in keyword:
        sum_hash += ord(char)
    return sum_hash%buckets
    # out = 0
    # for s in keyword:
    #     out = (out + ord(s)) % buckets
    # return out
print(hash_string('a',12))
# >>> 1
print(hash_string('b',12))
# >>> 2
print(hash_string('a',13))
# >>> 6
print(hash_string('au',12))
# >>> 10
print(hash_string('udacity',12))
# >>> 11


# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    # i = 0
    htable = []
    # while i < nbuckets:
    #     bucket = []
    #     htable.append(bucket)
    #     i += 1
    for n in range(0,nbuckets):
        htable.append([])
    return htable

table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]
print hashtable_get_bucket(table, "Brick")
#>>> []
print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]




# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
        return index.get(keyword)
        # return index[keyword]
    else:
        return None


# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>
# For example, this procedure returns a list of all the courses offered
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# You do not need to use this code if you do not want to and may find another,
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns
# True if the input course is offered in the input hexamester, and returns
# False otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012')
#>>> True

#print is_offered(courses, 'cs003', 'apr2012')
#>>> False

# (Note: it is okay if your procedure produces an error if the input
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    if course in courses_offered(courses, hexamester):
        return True
    else:
        return False

print is_offered(courses, 'cs101', 'apr2012')
#>>> True
print is_offered(courses, 'cs003', 'apr2012')
#>>> False
print is_offered(courses, 'cs001', 'jan2044')
#>>> True
print is_offered(courses, 'cs253', 'feb2012')
#>>> False

# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    offered = []
    for sem in courses:
        # offered = courses[c]
        # print(offered)
        if course in courses[sem]:
            offered.append(c)
    return offered

print when_offered (courses, 'cs101')
#>>> ['apr2012', 'feb2012']
print when_offered(courses, 'bio893')
#>>> []

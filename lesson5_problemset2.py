# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.
import string
alphabet = list(string.ascii_lowercase)
# print(alphabet)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n
def shift(letter):
    # indx = alphabet.index(letter) + 1 if (alphabet.index(letter) + 1) < len(alphabet) else 0
    # return alphabet[indx]

    indx = (alphabet.index(letter) + 1) % len(alphabet)
    return alphabet[indx]

print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a




# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.
import string
alphabet = list(string.ascii_lowercase)

# print(alphabet)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n


def shift_n_letters(letter, n):
    indx = (alphabet.index(letter) + n) % len(alphabet)
    return alphabet[indx]



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i





# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
import string
alphabet = list(string.ascii_lowercase)

def build_htable(n):
    htable = {" ": " "}
    for char in alphabet:
        htable[char] = alphabet[(alphabet.index(char) + n) % len(alphabet)]
    # print htable
    return htable

def rotate(jibber, n):
    # Your code here
    message = ""
    htable = build_htable(n)
    for i in range(0, len(jibber)):
        message += htable[jibber[i]]
    return message

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???

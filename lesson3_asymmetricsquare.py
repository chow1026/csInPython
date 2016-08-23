# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(lsts):
    #Write your code here
    i = 0
    while i < len(lsts):
        if len(lsts[i]) <> len(lsts): return False
        j = 0
        while j < len(lsts[i]):
            if int(lsts[i][j]) <> int(-lsts[j][i]): return False
            j += 1
        i += 1
    return True
# Test Cases:

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

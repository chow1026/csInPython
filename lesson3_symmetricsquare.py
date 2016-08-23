# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(lsts):
    i = 0
    while i < len(lsts):
        if len(lsts[i]) <> len(lsts):
            return False
        j = 0
        while j < len(lsts[i]):
            print("["+ str(i) + "][" + str(j) + "]: " + str(lsts[i][j])
            + "  vs  ["+ str(j) + "][" + str(i) + "]: " + str(lsts[j][i]))
            if lsts[i][j] <> lsts[j][i]:
                return False
            j += 1
        i += 1
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
# #>>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
#>>> False

print(symmetric([[1, 2],
                [2, 1]]))
# #>>> True

print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
# #>>> False

print(symmetric([[1,2,3],
                [2,3,1]]))
# #>>> False

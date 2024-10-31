#The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
def h_index(cite):
    #First we sort the number os citations in descending manner
    cite.sort(reverse=True)
    #We initiaize our h index
    h_index = 0
    #The index is the index number when the number of citations is greater than or equal to its index
    for i, c in enumerate(cite):
        #If the number of citations is greater than or equal to its index, it is the h index
        if c >= i + 1:
            #We get the h_index
            h_index = i + 1
        #Else we break
        else:
            break
    return h_index

        

print(h_index([33, 30, 20, 15, 7, 6, 5, 4]))
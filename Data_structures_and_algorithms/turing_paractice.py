
def frog_tongue(X, Y, S):
    #Implementing an O(n) solution using a dictionary or hash map to store data
    dict={}
    #Returns list of flies that can be trapped by frogs
    ans=[]
    #Store each value of the position of the frog in a dictionary
    for a, num in enumerate(X):
        dict[a]=num
    #Start with the first frog at position zero
    i=0
    #Iterate through both lists
    while i<len(X):
        #Initialize count of flies for every frog
        count=0
        #Iterate through the list that holds the position of the fly and increase count if condition is met
        for j in range(len(Y)):
            if abs(dict[i]-Y[j])<=S[i]:
                count+=1
        #Append count to answer list
        ans.append(count)
        i+=1
        #Increment i
    return ans

    


print(frog_tongue([4,4,6], [2,3,5,7], [2,2,3]))
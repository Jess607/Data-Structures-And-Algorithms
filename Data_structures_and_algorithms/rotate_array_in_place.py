#Rotating an array is a fairly easy operation all we have to do is basically swap the array arrangement by the number of steps specified
def rotate_array_in_place(arr,k):
    #First we get the length of the array which is used to enable the swap
    length=len(arr)
    #The edge case is when the number of rotations is less than the length of the array, in this case we use a modulo to get the number of rotations to undertake
    k=k%length
    #If k is not zero meaning no swap is meant to happen, we swap our elements
    if k!=0:
        #arr[:k], arr[k:]=arr[-k:], arr[:length-k]
        arr[:k], arr[k:]= arr[length-k:], arr[:length-k]

arr=[-1,-100,3,99]
rotate_array_in_place(arr,2)
print(arr)




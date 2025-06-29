#The objective of the problem is to find two lines that together with the x-axis form a container, such that the container contains the most water.
def max_container(height):
    #To solve the problem, we will be leveraging two pointers, one to the left and another to the right,the container with the most water is the one with the highest area that is length multiplied by width
    #The left pointer will start at index 0 and the right pointer will start at the end of the container
    #Also initialize max area to 0
    left, right=0, len(height)-1
    max_area=0
    #Next we iterate through the entire container
    while left<right:
        #Calculate the max area
        max_area=max(max_area, ((right-left)*min(height[left], height[right])))
        #If left is higher than right, move right towards the lft else move left towards the right, the idea is to find a higher container boundary
        if height[left]>height[right]:
            right-=1
        else:
            left+=1

    return max_area


print(max_container([1,8,6,2,5,4,8,3,7]))



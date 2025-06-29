def candy(list_of_children):
    len_of_list=len(list_of_children)
    left_pass=[1]*len_of_list
    right_pass=[1]*len_of_list
    for i in range(1, len_of_list):
        if list_of_children[i]>list_of_children[i-1]:
            left_pass[i]=left_pass[i-1]+1
    for i in range(len_of_list-2, -1, -1):
        if list_of_children[i]>list_of_children[i+1]:
            right_pass[i]=right_pass[i+1]+1

    number_of_candies=sum(max(right_candies, left_candies) for right_candies, left_candies in zip(left_pass, right_pass))
    return number_of_candies


print(candy([1,2,2]))
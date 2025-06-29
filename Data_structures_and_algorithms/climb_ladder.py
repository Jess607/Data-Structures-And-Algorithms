############Time inefficient###############
def climb_ladder(arr, arr_two):
    set_arr=set(arr)
    lis=[]
    for i in arr_two:
        new_arr=list(set_arr)
        new_arr.append(i)
        new_arr.sort(reverse=True)
        lis.append(new_arr.index(i)+1)
        set_arr.add(i)
    return lis



#################Better implementation#########
def climb_ladder(ranked, player):
# Write your code here
    ranked = sorted(set(ranked), reverse=True)  # Unique rankings in descending order
    result = []
    index = len(ranked)  # Start from the end of ranked list

    for score in player:
        while index > 0 and score >= ranked[index - 1]:
            index -= 1  # Move up in ranking if score is greater or equal
        result.append(index + 1)  # Rank is 1-based

    return result



print(climb_ladder([100,90,90,80], [70,80,105]))
set_arr=set([1,2,3,3,3,5])
#print(list(set_arr))
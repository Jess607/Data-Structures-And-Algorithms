def ice_cream_parlor(m, arr):
    dict={}
    for i, num in enumerate(arr):
        if m-num in dict:
            return dict[m-num]+1, i+1
        dict[num]=i
    return 'No'


print(ice_cream_parlor(6, [1,2,3,4,5]))

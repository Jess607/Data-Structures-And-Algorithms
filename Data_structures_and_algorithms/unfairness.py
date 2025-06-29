def unfairness(k, arr):
    arr.sort()
    i=0
    ans=sum(arr)
    while i<len(arr)-k +1:
        curr_ans = arr[i + k - 1] - arr[i]
        ans=min(ans, curr_ans)
        i+=1
    return ans



print(unfairness(5,
[4504,1520,5857
,4094,
4157,
3902,
822,
6643,
2422,
7288,
8245,
9948,
2822,
1784,
7802,
3142,
9739,
5629,
5413,
7232]))
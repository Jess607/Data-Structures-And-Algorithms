def add_two_numbers(l1, l2):
    temp1=l1
    temp2=l2
    lis_a=[]
    lis_b=[]
    str_a=''
    str_b=''
    while temp1:
        lis_a.append(temp1.val)
        temp1=temp1.next
    while temp2:
        lis_b.append(temp2.val)
        temp2=temp2.next


    for i in range(len(lis_a), -1, -1):
        str_a+=str(lis_a[i])

    for j in range(len(lis_b), -1, -1):
        str_b+=str(lis_b[j])

    answer= int(str_a) + int(str_b)
    return answer


lsi=[2,3,4]
lsi.reverse()
print(lsi)
def inc(li):                                                #function inc will increment the number by 1
    n = len(li) - 1
    while li[n] == 9:
        li[n] = 0
        n -= 1
    if (n > -1):
        li[n] = li[n] + 1
    if (n == -1):
        li.insert(0, 1)

    i = 0
    while li[i] == 0:                                       #deleting precedding 0s
        li.pop(0)

    return li

x=int(input("Enter the number of digit in firt list"))      #Getting size of the list
print("Enter the elements of list:-")                       #Getting elements of  list
li=[]
for i in range(x):
    s=int(input())
    li.append(s)

print("entered list:-",li)


print("List after incrementing by 1",inc(li))

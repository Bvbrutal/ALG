def select_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    print(li)
    return None

li=[7,2,3,9,5,6,4,1]
select_sort(li)
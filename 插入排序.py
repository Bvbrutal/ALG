def insert_sort(li):
    for i in range(1,len(li)):
        tmp=li[i]
        j=i-1
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j -= 1
        li[j+1]=tmp
    print(li)
    return None

li=[7,2,3,9,5,6,4,1]
insert_sort(li)
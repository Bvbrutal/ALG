

def bubble_sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(1,len(li)-i):
            if li[j-1]>li[j]:
                li[j-1],li[j]=li[j],li[j-1]
                exchange=True
        if not exchange:
            break
    print(li)
    return None

li=[7,2,3,9,5,6,4,1]
bubble_sort(li)
import sys
sys.setrecursionlimit(10000)
import random
from cal_time import cal_time


def pa(li,left,right):
    tmp = li[left]
    while left<right:
        while left<right and tmp<=li[right]:
            right-=1
        li[left] = li[right]
        while left<right and tmp>=li[left]:
            left+=1
        li[right] = li[left]
    li[left]=tmp
    return left

def quick_sort(li,left,right):
    if left<right:
        mid=pa(li,left,right)
        quick_sort(li, left, mid-1)
        quick_sort(li,mid+1,right)
    return li

@cal_time
def quick_sort_(li, left, right):
    li=quick_sort(li, left, right)
    return li

#
# li=[7,3,2,9,5,6,4,1]
li=[random.randint(0,100) for i in range(100)]
print(li)
# pa(li,0,len(li)-1)
li=quick_sort_(li,0,len(li)-1)
print(li)
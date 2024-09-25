import random
def findkth(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)
    left=[i for i in arr if i>pivot]
    right=[i for i in arr if i<pivot]
    mid=[i for i in arr if i==pivot]
    return findkth(left)+mid+findkth(right)
arr=[15,12,13,10,9,8]
print(findkth(arr))

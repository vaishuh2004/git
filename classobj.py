#st=[25,23,24,21,26,28,29,63,54,21]



arr=[1,11,21,10,13,16,15]
for i in range(len(arr)-1):
    min=i
    for j in range(i+1,len(arr)):
        if arr[min]>arr[j]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
    print(arr)
print(arr)
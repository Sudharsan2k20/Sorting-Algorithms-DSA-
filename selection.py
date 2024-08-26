arr = [4,2,5,3,1]
for i in range(0, len(arr)-1):
    pos=i
    for j in range(i+1, len(arr)):
        if arr[j]<arr[pos]:
            pos=j
    arr[pos], arr[i] = arr[i], arr[pos]
print(arr)
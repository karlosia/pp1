def f(arr):
    i=0
    while i<len(arr)-1:
        if arr[i]!=arr[i+1]:
            return i+1
        i=i+1
    return None


print(f([7,7,7,7,7,5,7,7]))

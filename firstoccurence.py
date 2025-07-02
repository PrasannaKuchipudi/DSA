def first(arr,x):
    low=0
    high=len(arr)-1
    first=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            first=mid
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return first
arr=[1,2,3,3,3,4,5,6]
x=3
result=first(arr,x)
print(f"The first occurence of {x} is at index {result}.")
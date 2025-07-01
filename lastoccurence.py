def lastoccurence(arr,x):
    low=0
    high=len(arr)-1
    last=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            last=mid
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return last
arr=[1,2,3,3,3,4,5,6]
x=3
result=lastoccurence(arr,x)
print(f"The Last Occurence of {x} is at index {result}")
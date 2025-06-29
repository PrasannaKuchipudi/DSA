def searchInsert(arr,x):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,2,3,5]
x=4
result=searchInsert(arr,x)
print(f"The insert position of {x} is at index",result)
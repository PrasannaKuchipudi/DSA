def ceil(arr,x):
    arr.sort()
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=arr[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[10,20,40,50,30]
x=25
result=ceil(arr,x)
print("The ceil of an array is:",result)
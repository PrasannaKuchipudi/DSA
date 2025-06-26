def lowerbound(arr,x):
    arr.sort()
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
arr=[1,2,3,4,5]
x=1
result=lowerbound(arr,x)
print(result)
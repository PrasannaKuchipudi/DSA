def upperbound(arr,x):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,2,2,3]
x=2
result=upperbound(arr,x)
print("The upper bound is the index:",result)
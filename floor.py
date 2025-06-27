def floor(arr,x):
    arr.sort()
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ans=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
arr=[10,20,30,40,50]
x=25
result=floor(arr,x)
print("The floor element is:",result)

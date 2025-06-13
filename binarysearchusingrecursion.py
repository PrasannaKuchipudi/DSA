def binarysearch(arr,low,high,target):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return binarysearch(arr,low,high-1,target)
        else:
            return binarysearch(arr,0,high,target)
    else:
        return -1
arr=[1,2,3,4,5]
target=2
result=binarysearch(arr,0,len(arr)-1,target)
if result==(-1):
    print(target,"is not found")
else:
    print(target,"is found at",result,"index")


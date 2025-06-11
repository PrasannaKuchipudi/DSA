def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[1,2,3,4,5]
target=3
result=linearsearch(arr,target)
if target!=1:
    print(target,"is found at",result,"index")
else:
    print(target,"is not found")

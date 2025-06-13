def floor_sqrt(num):
    if num==0 or num==1:
        return num
    low,high=0,num
    ans=0
    while low<=high:
        mid=(low+high)//2
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
num=int(input("Enter a number:"))
result=floor_sqrt(num)
print(result)


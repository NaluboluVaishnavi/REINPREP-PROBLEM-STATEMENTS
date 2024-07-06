n=int(input())
arr=list(map(int,input().split()))
d={}
if n==1:
    print(arr[0])
else:
    for num in arr:
        if num not in d:
            d[num]=1
        else:
            d[num]+=1
    x=sorted(d.items(),key=lambda x:x[1],reverse=True)
    if x[0][1]==x[1][1]:
        print(-1)
    else:
        print(x[0][0])                    
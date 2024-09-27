n=int(input())
a=list(map(int,input().split()))
non_zero=[]
for i in a:
 if i!=0:
 non_zero.append(i)
num=a.count(0)
res=non_zero+[0]*num
print(" ".join(map(str,res)))

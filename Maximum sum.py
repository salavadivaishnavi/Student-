n=int(input())

l=list(map(int,input().split()))

sm,mx=0,0

for i in l:

 sm+=i

 mx=max(mx,sm)

 if sm<0:

 sm=0

print(mx)

s=input()
v="aeiou"
cc=0
vc=0
for i in s:
 if i in v:
 vc+=1
 else:
 cc+=1
print("Number of vowels:",vc)
print("Number of consonants:",cc)

s=list(input()) #W,R,B house,minimise the badness
#try to change the white color house to the color of prev house
#edge case - string s starts with a W house - try to find the nearest R or B house and change it to that color
for i in range(len(s)):
    if s[i]=="W":
        if i==0:
            for j in range(1,len(s)):
                if s[j]!="w":
                    s[i]=s[j]
                    break
        else:
            s[i]=s[i-1]
badness=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        badness+=1
print(badness)                    

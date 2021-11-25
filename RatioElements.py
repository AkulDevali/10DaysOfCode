n=int(input("Enter Size\n"))
s=input("Enter array elements\n").split()
arr=[]
for i in s:
    arr.append(int(i))

pc=0
nc=0
zc=0

for i in arr:
    if i >0:
        pc+=1
    elif i<0:
        nc+=1 
    else:
        zc+=1 
print((round((pc/n),6)),(round((nc/n),6)),round((zc/n),6),sep="\n")
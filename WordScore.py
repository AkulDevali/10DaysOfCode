count = 0
str=input()
for i in range(len(str)):
    if str[i] in {'a','e','i','o','u'}:
        count+=1
print(count)
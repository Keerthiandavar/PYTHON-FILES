str=input()
num=int(input())
str1=""
for i in range(len(str)):
    if i != num:
        str1=str1+str[i]
print(str1)
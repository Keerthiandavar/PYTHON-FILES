g= input()
h=k=0
for i in g:
    if i.isdigit():
        h=h+1
    elif i.isalpha():
        k=k+1
print("Characters=",k)
print("Digits=",h)




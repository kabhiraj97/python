num=int(input("enter a number: "))
i=0
j=1
for a in range(num):
    print(i,end=" ")
    k=i+j
    i=j
    j=k
    
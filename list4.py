idx=[2,3,4,5,7,9,11,13,15,19]
count=0
for i in idx:
    if i%2==0:
        count=count+1
        i+=1
print(f"total even num in a list: {count}")
c=len(idx)-count
print(f"total odd num in a list: {c}")
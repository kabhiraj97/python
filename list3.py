idx=[10,11,12,13,14,15,16]
product=1
total=sum(idx)
average=total//len(idx)
maximum=max(idx)
minimum=min(idx)
print(f"Total sum of the list: {total}")
print(f"Average of the list: {average}")
print(f"Maximum num present in list: {maximum}")
print(f"Minimum num present in list: {minimum}")
for i in idx:
    product=product*i
    print(f"Product of list: {product}")
print(f"total product of the list: {product}")    
    



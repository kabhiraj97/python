# Write a Python program to sort tuples using Lambda.
num=(5,4,8,12,9,11,3,6,7,10)
# num1=list(num)
sort=sorted(num,key=lambda y:y)
print(sort)
num2=tuple(sort)
print(num2)
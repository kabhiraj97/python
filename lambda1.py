a=lambda x,y,z:print(x*y*z)
a(4,2,2)

# Write a Python program to square and cube every number in a given list of integers using Lambda
numbers=[1,2,3,4,5,6]
squared=list(map(lambda x: x**2,numbers))
cubic=list(map(lambda x: x**3,numbers))
print(squared)
print(cubic)

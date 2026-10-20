# WAP to define a function for sum, difference, multiplication and division
# def m(a,b):
#     print(a+b)
#     print(b-a)
#     print(a*b)
#     print(a%b)

# m(3,8)

# WAP to print the even number from a range by defining functions
# def num(a,b):
#     for num in range(a,b+1):
#         if num%2==0:
#             print(num,end=" ")
  
# num(1,10)

# Write a Python function to find the maximum of three numbers.
# def maximum(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     else:
#         print(c)

# maximum(100,400,200)

# Write a Python function to sum all the numbers in a list.


# def sum_list(x):
#     total= 0
#     for num in x:
#         total=total+num
#     return total
    

# num_list=[1,2,3,4,5,6]
# result=sum_list(num_list)

# print(f"The sum of the list {num_list} is: {result}")

# Write a Python function to multiply all the numbers in a list.

# def prod_list(x):
#     product=1
#     for num in x:
#         product=product*num
#     return product
    

# num_list=[1,2,3,4,5,6]
# result=prod_list(num_list)

# print(f"The product of the list {num_list} is: {result}")

# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

# def calculate_factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
        
#     if n == 0 or n == 1:
#         return 1
        
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
        
#     return result
# number = 5
# output = calculate_factorial(number)
# print(f"The factorial of {number} is: {output}")

# Write a Python program to print the even numbers from a given list.
sample_list = [11,22,33,44,55,66,77,88]
def print_even_num(numbers):
    for i in numbers:
        if i%2==0:
            print(i, end=" ")

print_even_num(sample_list)            



    


    


numbers=[1,2,3,4,5,6,7,8]
even_nums=list(filter(lambda x: x%2==0,numbers))
odd_nums=list(filter(lambda x: x%2==1,numbers))
print(even_nums)
print(odd_nums)
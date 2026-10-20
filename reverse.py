num=int(input("enter a number: "))
revnum=0
num1=num
if (num < 0):
    num = num*-1
while num>0:
    revnum=(revnum*10)+(num%10)
    num=num//10
if (num1 < 0):
    revnum = revnum * -1
print(revnum)
# if num1==revnum:
#     print("number is pallindrome")
# else:
#     print("number is not pallindrome")    
    
    

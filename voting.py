# age=15
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")    


# age=18
# if age>=21:
#     print("Eligible to participate election")
# else:
#     print("Not eligible to participate election")

age=int(input("enter the age"))
if age>=21:
    print("Eligible to vote and participate in election")
elif age>=18 and age<21:
    print("Eligible to vote only")
else:
    print("Not eligible for both")    

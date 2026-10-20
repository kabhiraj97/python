# a={"name":"Kumar","age":31}
# b={"location":"Bangalore","department":"IT"}
# print(a)
# print(a["name"])
# a["Location"]="Bangalore"
# print(a)
# del a["age"]
# print(a)
# a["name"]="Kumar Abhiraj"
# print(a)
# print(a["name"],b["department"])


# a={"name","age","department"}
# b={"Kumar Abhiraj",31,"IT"}

# new_dict=dict(zip(a,b))
# print(new_dict)


# a={"name":"Kumar","age":31}
# b={"location":"Bangalore","department":"IT"}

# c={**a,**b}
# print(c)


# person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
# print(person["name"],person["address"]["zip"])


# student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
# print(student["grades"]["history"])


# a={"name":"Kumar","age":31}
# b={"location":"Bangalore","department":"IT"}
# c={**a,**b}
# c.clear()
# print(c)


a={"name","age","location"}
b=25
c=dict.fromkeys(a,b)
print(c)

dict = {"name":"kumar", "name1":"abhiraj"}
dict["name"] = dict.pop("name1")

print(dict)

dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_remove = ["b", "d"]
for i in keys_remove:
    dict.pop(i)
print(dict)






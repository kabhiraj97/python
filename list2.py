idx=[100,300,500,700,900]
print(idx)
idx[2]=200
print(f"the second element replaced{idx}")
idx.append(600)
print(f"the updated list: {idx}")
idx.insert(2,300)
print(f"number inserted at 2nd position: {idx}")
idx.remove(300) #removed element by value
print(idx)
idx.remove(600) #removed element by value
print(idx)
idx.remove(idx[3]) #removed element by index 
print(idx)
idx.remove(idx[0]) #removed element by index 
print(f"The updated list : {idx}")

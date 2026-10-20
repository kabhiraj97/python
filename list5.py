idx=[4,7,6,3,1,5,2,9,8]
#print(idx[::-1])
idx.reverse()
print(f"Reverse for the list of element: {idx}")
idx.sort()
print(f"Sorting for the list of element: {idx}")
idx2=idx.copy()
print(f"Copy of list of element: {idx2}")
idx3=idx+idx2
print(f"combination of the 2 list: {idx3}")
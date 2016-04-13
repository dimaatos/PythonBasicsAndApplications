objects = [1,1,True] 

unique = []

for obj in objects:
    if obj not in unique:
        unique.append(obj)

print(len(unique))
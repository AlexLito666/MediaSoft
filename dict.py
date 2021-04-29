my_dict = {"name":"ivan", "lastname":"ivanov"}
new_dict = {}

for key, value in my_dict.items():
    key, value = value, key
    new_dict[key] = value

print(new_dict)
    

import os 
directory_path = '/users'
contents = os.listdir(directory_path)
for item in contents:
    print(item)
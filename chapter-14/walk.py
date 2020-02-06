import os

my_dir = '/home/lark/Documents/'

for root, dis, files in os.walk(my_dir):
    for file_name in files:
        print (os.path.join(root, file_name))
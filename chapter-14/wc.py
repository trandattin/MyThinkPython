def linecount(filename):
    count = 0 
    for line in open(filename):
        count += 1
    return count

print(linecount('/home/lark/Documents/my-think-python/chapter-14/wc.py'))
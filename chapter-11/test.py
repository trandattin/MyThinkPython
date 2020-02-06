def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

t = {1,3,2,4,5,6}
print(has_duplicates(t))
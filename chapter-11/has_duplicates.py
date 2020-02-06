def has_duplicates(t):
    d = dict()
    for i in t:
        x = d.setdefault(i)
        if x == 2:
            return True
        return False
t = [1,2,3,4,5,6,6]
print(has_duplicates(t))
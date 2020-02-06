def nested_sum(t):
    for i in t:
        for j in i:
            j += j
    return j

def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res


def middle(t):
    return t[1:-1]   


def chop(t):
    t.pop(0)
    t.pop(-1) 
    

def is_sorted(t):
    for i in range(len(t)):
        if t[i] <= t[i+1] :
            return True
        else:
            return False

def is_anagram(string1,string2):
    return sorted(string1) == sorted(string2)


def has_duplicates(t):
    '''
    Write a function called has_duplicates that takes a list and returns True if there
    is any element that appears more than once. It should not modify the original list
    '''
    for i in t:
        x = t.count(i)
        if x == 2:
            return True
    return False

has_duplicates()
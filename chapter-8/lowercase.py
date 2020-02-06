def any_lowercase1(s):
    # Check if the frist word is lower return True
    for c in s:
        if c.islower():
            return True
        else:
            return False
        


def any_lowercase2(s):
    # Checks if string 'c' is lowercase or not; and returns string 'True';
    # Returns 'True' everytime, given argument does not matter;
    for c in s:
        if 'c'.islower():
            return 'True' 
        else:
            return 'False'


def any_lowercase3(s):
    # Check if the last word is lower return True
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    # Checks if there is ANY lowercased letter in given string and returns boolean;
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    # Checks every letter if it is not lowercased and returns boolean if all the
    # letters in string are lowercased or not;
    for c in s:
        if not c.islower():
            return False
        return True
    
print(any_lowercase5(''))


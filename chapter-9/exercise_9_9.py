def guest_age(age_of_son,age_of_mom):
    age_of_mom = age_of_mom - age_of_son
    age_of_son = 0
    count = 0
    while age_of_mom < 100:
        if age_of_son == int(str(age_of_mom)[::-1]):
            count += 1
            print(age_of_son, end=' ')
            print(age_of_mom)
        age_of_son += 1
        age_of_mom += 1

    return count    
print(guest_age(0,18))
    
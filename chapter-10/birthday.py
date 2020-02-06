import random
from exercise_list import has_duplicates

def random_birthday(students):
    box = []
    for i in range (students):
        t = random.randint(1,365)
        box.append(t)
    return box

def count_matches(students,samples):
    count = 0
    for i in range(samples):
        t = random_birthday(students)
        if has_duplicates(t):
            count += 1
    return count

num_students = 72
num_simulations = 1
count = count_matches(num_students,num_simulations)
random_birthday(num_students)
print(count)
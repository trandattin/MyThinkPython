'''Exercise 16.2. The datetime module provides time objects that are similar to the Time objects
in this chapter, but they provide a rich set of methods and operators. Read the documentation at
http: // docs. python. org/ 3/ library/ datetime. html .

1. Use the datetime module to write a program that gets the current date and prints the day of
the week.

2. Write a program that takes a birthday as input and prints the user’s age and the number of
days, hours, minutes and seconds until their next birthday.

3. For two people born on different days, there is a day when one is twice as old as the other.
That’s their Double Day. Write a program that takes two birth dates and computes their
Double Day.

4. For a little more challenge, write the more general version that computes the day when one
person is n times older than the other.'''

from datetime import datetime


def compute_today():
    '''Return datetime object as the date, time at present'''
    return datetime.today()


def format_day(day):
    '''Format date string in mm/dd/yyyy format

    day: string
    return: datetime object
    '''
    return datetime.strptime(day, "%m/%d/%Y")


def convert_weekday():
    '''Convert a datetime object and return string format'''
    today = compute_today()
    return today.strftime("%A")


def compute_next_bday(day):
    '''Return datetime object as next birthday from preset

    day: string as mm/dd/yyyy format
    '''
    today = compute_today()
    birthday = format_day(day)

    next_bday = birthday.replace(year=today.year)

    if next_bday < today:
        next_bday = bday_this_year.replace(year=today.year+1)

    return next_bday


def compute_until_next_bday(day):
    ''' Return time.delta object as number of days

    day: string as mm/dd/yyyy format
    '''
    return type(compute_next_bday(day) - compute_today())


def compute_age(day):
    ''' Return time.delta object as the age

    day: string as mm/dd/yyyy format
    '''
    birthday = format_day(day)
    next_bday = compute_next_bday(day)
    last_bday = next_bday.replace(year=next_bday.year-1)

    return last_bday.year - birthday.year


def compute_double_date(n=3):
    '''Compute the double's days of two brithday in n times

    n = integer of the times
    return: datetime object
    '''
    bday1 = datetime(day=21, month=11, year=2000)
    bday2 = datetime(day=24, month=2, year=2018)
    print(bday1)
    print(bday2)

    age_diff = abs(bday1 - bday2)
    d1 = max(bday1,bday2)
    double_days = age_diff * n/2 + d1

    print("Double Day is: ")
    print(double_days)

print(format_day("11/21/2000"))


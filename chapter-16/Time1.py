import datetime

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

class Date:
    """"""

def print_time(time):
    '''Print time format'''
    print (('%.2d : %.2d : %.2d') % (time.hour, time.minute, time.second))


def is_after(t1,t2):
    """Return a boolean value in compart to time object
    t1,t2: time object
    """
    return (t1.hour, t1.minute, t1.second) < (t2.hour, t2.minute, t2.second)


def time_to_int(time):
    """Computes the number of seconds since midnight

    time: Time object
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """Makes a new Time object

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def valid_time(time):
    """Checks whether a Time object satisfies the invariants"""
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time(t1, t2):
    """Adds two time objects"""
    assert valid_time(t1) or valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def mul_time(t1, distance):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * distance
    return int_to_time(seconds)


def main():
    time = Time()
    time.hour = 1
    time.minute = 59
    time.second = 30

    t1 = Time()
    t1.hour = 2
    t1.minute = 40
    t1.second = 59

    t2 = Time()
    t2.hour = 2
    t2.minute = 40
    t2.second = 59

    done = add_time(t1, t2)
    print_time(done)

if __name__ == "__main__":
    main()
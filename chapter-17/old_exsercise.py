
class Time:
    """Represents a point in 2-D space

    attributes: x,y
    """
    def __init__(self, hour=0, minute=0, second=0):
       minutes = hour * 60 + minute
       self.seconds = minutes * 60 + second

    def __str__(self):
        minute, second = divmod(self.seconds, 60)
        hour, minute = divmod(minute, 60)
        return ('%.2d:%.2d:%.2d' % (hour, minute, second))

    def __add__(self, other):
        """Adds two time object or a Time object and a number

        other: Time object a number of second
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self,other):
        return self.__add__(other)

    def add_time(self, other):
        """Add two time object"""
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print(str(self))

    def time_to_int(self):
        """Computes the number of second since midnight"""
        return self.seconds

    def increment(self, seconds):
        """Return a new Time that is the sum of this time and seconds"""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_vaild(self):
        """Checks whether a Time object satisfies the invariants"""
        return self.seconds > 0 and self.seconds < 24*60*60

def int_to_time(seconds):
    """Make a new Time object

    seconds: int time since midnight
    """
    return Time(0,0,seconds)

class Point:
    """Repres space a point in 2-D space

    attributes: x, y
    """
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)

    def __add__(self, other):
        """Add two Point object or a Point object and a tuple"""
        if isinstance(other, Point):
            return (self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return (self.x + other[0], self.y + other[1])
        else:
            msg = "Something is wrong"
            raise TypeError(msg)

    def __radd__(self, other):
        return self.__add__(other)


def main():
    time1 = Time(4,5,6)
    time1.print_time()


if __name__ == '__main__':
    main()


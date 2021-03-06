import math


class Date(object):

    def __init__(self, day, decade, month, year, era=3):
        super(Date, self).__init__()
        self.day = day
        self.decade = decade
        self.month = month
        self.year = year
        self.era = era

    def __str__(self):

        def decade(i):
            return {
                1: "Декады Юности",
                2: "Декады Молодости",
                3: "Декады Зрелости",
                4: "Декады Старости"
            }[i]

        def month(i):
            return {
                1: "Месяца Цветения",
                2: "Месяца Пылевика",
                3: "Месяца Жареня",
                4: "Месяца Листопада",
                5: "Месяца Осеннего Дождепада",
                6: "Месяца Серебрянки",
                7: "Месяца Снегопада",
                8: "Месяца Стужения",
                9: "Месяца Капеля",
                10: "Месяца Весеннего Дождепада"
            }[i]

        def era(i):
            return {
                1: "Эры Неизвестности",
                2: "Эры Тьмы",
                3: "Эры Счастья",
                4: "Эры Смерти"
            }[i]

        return "%s %s %s %s %s %s %s" % \
               (self.day, "День",  decade(self.decade), month(self.month),
                self.year, "Года", era(self.era)
                if self.era else "")

    """For calling magic method __str__ -> 
        date_when_we_come = Date(3, 2, 8, 7410)
        print(date_when_we_come)"""

    def __repr__(self):
        return "[%s.%s.%s.%s.%s]" % \
               (self.day, self.decade, self.month, self.year, self.era)

    def to_string(self, long_format=True):
        return self.__str__() \
            if long_format else self.__repr__()

    """For calling magic method __repr__ -> 
        date_when_we_come = Date(3, 2, 8, 7410)
        print(repr(date_when_we_come))"""

    @classmethod
    def from_string(cls, string):
        li = string.strip("[").strip("]").split(".")
        if not len(li) == 5:
            raise ValueError("The given value is not a date!")
        else:
            return cls(int(li[0]), int(li[1]), int(li[2]), int(li[3]), int(li[4]))

    """For calling this method __repr__ -> 
        print(Date.from_string("[1.2.3.2.3]"))
        print(Date.from_string("[1.2.3.2.3]").to_string(False))"""

    def __int__(self):
        return self.day + (self.decade - 1) * 10 + (self.month - 1) * 40 + (self.year - 1) * 400

    def __complex__(self):
        return complex(self.__int__(), self.era)

    """For calling this method __int__ & __complex__ -> 
        date_when_we_come = Date(3, 2, 8, 7410)
        print(int(date_when_we_come))
        print(complex(date_when_we_come))"""

    @classmethod
    def from_complex(cls, x):
        year, month, decade, day = 0, 0, 0, 0
        year = math.floor(int(x.real)/400) + 1
        if int(x.real) % 400 == 0:
            year -= 1
        elif int(x.real) > 400:
            days = int(x.real) - (400 * (year - 1))
        else:
            days = int(x.real)

        month = math.floor(days/40) + 1
        if days % 40 == 0:
            month -= 1
        elif days > 40:
            dayz = days - (40 * (month-1))
        else:
            dayz = days

        decade = math.floor(dayz/10) + 1
        if dayz % 10 == 0:
            decade -= 1
        elif dayz > 10:
            day = dayz - (10 * (decade-1))
        else:
            day = dayz
        return cls(day, decade, month, year, int(x.imag))

    """For calling this method from_complex_ -> 
        date_when_we_come = Date(3, 2, 8, 7410)
        print(Date.from_complex(2963893+3j))
        print(date_when_we_come)"""

    @classmethod
    def from_int(cls, i):
        return cls.from_complex(complex(i))

    """For calling this method from_complex_ -> 
        date_when_we_come = Date(3, 2, 8, 7410)
        print(Date.from_int(2234333))"""

    @staticmethod
    def days_since_start_of_era(date):
        return int(date) - 1

    @property
    def current_day_since_start_of_era(self):
        return int(self)

    @staticmethod
    def decades_since_start_of_era(date):
        return math.floor(int(date)/10)

    @property
    def current_decade_since_start_of_era(self):
        return math.floor(int(self)/10)

    @staticmethod
    def months_since_start_of_era(date):
        return math.floor(int(date)/40)

    @property
    def current_month_since_start_of_era(self):
        return math.floor(int(self)/40) + 1

    @staticmethod
    def years_since_start_of_era(date):
        return math.floor(int(date)/400)

    @property
    def current_year_since_start_of_era(self):
        return math.floor(int(self)/400) + 1

    """For calling this method -> 
        date = Date(3, 2, 8, 7410)
        print(Date.months_since_start_of_era(1212121))"""

    @staticmethod
    def is_working_day(date):
        return 1 < date.day < 10

    @staticmethod
    def is_decade_start_celebration(date):
        return date.day == 1 and 1 < date.decade < 4

    @staticmethod
    def is_decade_end_celebration(date):
        return date.day == 10 and 1 < date.decade < 4

    @staticmethod
    def is_month_start_celebration(date):
        return date.day == 1 and date.decade == 1

    @staticmethod
    def is_month_end_celebration(date):
        return date.day == 10 and date.decade == 4

    """Methods for equality
        __eq__ (==) equal
        __ne__ (!=) not equal
        __lt__ (<) less than
        __gt__ (>) greater than
        __le__ (<=) less than or equal
        __ge__ (>=) greater than or equal
    """
    def __eq__(self, other):
        return complex(self) == complex(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return int(self) < int(other) if self.era <= other.era else False

    def __gt__(self, other):
        if self.era >= other.era:
            return int(self) > int(other)
        else:
            return False

    """For calling this method -> 
        result = Date(1, 2, 2, 2, 3) < Date(1, 2, 2, 3, 3)
        print(result)"""

    def __le__(self, other):
        return True if self.__lt__(other) or self.__eq__(other) else False

    def __ge__(self, other):
        return True if self.__gt__(other) or self.__eq__(other) else False

    """Next magic methods:
        __add__ (self + other) add
        __radd__ (other + self) reflected add
        __sub__ (self - other) subtract
        __iadd__ (self += other) 
        __isub__ (self -= other)
    """

    def __add__(self, other):
        return self.from_complex(complex(self) + other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if int(self) - other < 0:
            return "Somewhere in the %s era"%(self.era - 1)
        else:
            return self.from_complex(complex(self) - other)

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    """Next methods"""

    def add_days(self, days):
        return self + days

    def add_decades(self, decades):
        return self + decades * 10

    def add_month(self, months):
        return self + months * 40

    def add_years(self, years):
        return self + years * 400

    @staticmethod
    def time_delta(date1, date2, absolute=True):
        return abs(int(date1) - int(date2)) if absolute else int(date1) - int(date2)
    
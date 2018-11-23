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

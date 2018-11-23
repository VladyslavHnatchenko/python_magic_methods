
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

        return "%s %s %s %s %s %s %s"%(self.day, "День",
                                       decade(self.decade),
                                       month(self.month),
                                       self.year, "Года",
                                       era(self.era) if self.era else "")


date_when_we_come = Date(3, 2, 8, 7410)
print(date_when_we_come)

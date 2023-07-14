class Tramvai():
    """ Класс предназначенный для моделирования механического трамвая """
    def __init__(self, type, year, sit_field) -> None:
        self.year = year
        self.sit_field = sit_field
        self.type = str(type).title()
        self.count_gas = 50
    
    def full_name(self):
        """ Выводит полное название травмвая """
        print(f"{self.type} tramvai created in {self.year} and have {self.sit_field} sit field.")

    def get_count_gas(self):
        """ Выводит обьем топливного бака """
        print(f"This {self.type} tramvai have {self.count_gas} litrs.")

class Battery():
    """ Класс предназначенный для моделирования батареи электрического трамвая """
    def __init__(self, volume) -> None:
        self.volume = volume

class ElecricalTramvai(Tramvai):
    """ Класс предназначенный для моделирования электрического трамвая """
    def __init__(self, year, sit_field) -> None:
        self.type = "electrical".title()
        self.battery = Battery(1500)
        super().__init__(self.type, year, sit_field)

    def get_voltage(self):
        """ Выводит ёмкость аккамулятора травмвая """
        print(f"This tramvai energi volume: {self.battery.volume}")

    def get_full_info(self):
        """ Выводит полную информацию о травмвае """
        print("This Tramvai configuration:")
        conf = {"Type":self.type, "Year":self.year, "Energi volume":self.battery.volume, "Sit field":self.sit_field}
        for Parm, val in conf.items():
            print(f"\t {Parm} : {val}")

    def get_count_gas(self):
        """ Переопределение метода получения ёмкости топливого бака """
        print(f"This {self.type} tramvai don't have gas.")

Tramvai("mechanic", 1990, 50).get_count_gas()
ElecricalTramvai(year=2010, sit_field=60).get_count_gas()
ElecricalTramvai(year=2016, sit_field=60).get_full_info()
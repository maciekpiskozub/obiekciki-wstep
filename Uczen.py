from Czlowiek import Czlowiek
class Uczen(Czlowiek):

    liczba_uczniow = 0


    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        Uczen.liczba_uczniow += 1

    def __str__(self):
        return f'{self.__imie}{self.__nazwisko}'


    def ucz_sie(self):
        print(f'{self.__imie}{self.__nazwisko} uczy sie!!')


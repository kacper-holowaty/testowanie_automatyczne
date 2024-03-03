class BrakPracownikaOPodanymID(Exception):
    pass

class PustyRejestr(Exception):
    pass

class Widok:

    @staticmethod
    def wyswietl_liste_pracownikow(lista_pracownikow):
        lista_obiektow = [str(pracownik) for pracownik in lista_pracownikow]
        print(lista_obiektow)

    @staticmethod
    def wyswietl_liste_wraz_z_wartososcia_dla_korporacji(lista_pracownikow):
        result = []
        for pracownik in lista_pracownikow:
            pracownik_str = str(pracownik)[:-1]
            wartosc = pracownik.oblicz_wartosc_dla_korporacji()
            pracownik_str += f', wartosc_dla_korporacji: {round(wartosc,1)}' + '}'
            result.append(pracownik_str)
        print(result)

class MetodyWspomagajaceRejestr:

    @staticmethod
    def sprawdz_klucz(pracownik, funkcja):
            try:
                value = funkcja(pracownik)
                if value is None:
                    return float('inf')
                elif isinstance(value, str):
                    return ord(value[0])
                else:
                    return value
            except AttributeError:
                return float('inf')
    
    @staticmethod
    def posortuj_pracownikow(rejestr, key=None):
        lista_pracownikow = list(rejestr.values())
        if key is None:
            key = lambda pracownik: (-pracownik.doswiadczenie, pracownik.wiek, pracownik.nazwisko)

        posortowani_pracownicy = sorted(lista_pracownikow, key=lambda pracownik: MetodyWspomagajaceRejestr.sprawdz_klucz(pracownik, key))
        return posortowani_pracownicy

    @staticmethod
    def wyszukaj_pracownikow_z_danego_miasta(rejestr, miasto):
        lista_pracownikow = list(rejestr.values())
        pracownicy_z_miasta = [pracownik for pracownik in lista_pracownikow if pracownik.adres_budynku.miasto == miasto]
        return pracownicy_z_miasta

class Rejestr:

    def __init__(self, pracownicy_w_rejestrze=None):
        self.rejestr = pracownicy_w_rejestrze if pracownicy_w_rejestrze else {}
        self.widok = Widok()
        self.klasaWspomagajaca = MetodyWspomagajaceRejestr()

    def dodaj_pracownika(self, pracownik):
        self.rejestr[pracownik.id] = pracownik
    
    def usun_pracownika(self, id_pracownika):
        if self.rejestr:
            if id_pracownika in self.rejestr:
                del self.rejestr[id_pracownika]
            else:
                raise BrakPracownikaOPodanymID()
        else: 
            raise PustyRejestr() 
    
    def dodaj_kilku_pracownikow(self, *pracownicy):
        for pracownik in pracownicy:
            self.dodaj_pracownika(pracownik)

    def wyswietlanie_listy_posortowanych_pracownikow(self, funkcja_sortujaca=None):
        posortowani_pracownicy = self.klasaWspomagajaca.posortuj_pracownikow(self.rejestr,funkcja_sortujaca)
        self.widok.wyswietl_liste_pracownikow(posortowani_pracownicy)

    def wyswietlanie_listy_pracownikow_z_danego_miasta(self, miasto):
        pracownicy_z_miasta = self.klasaWspomagajaca.wyszukaj_pracownikow_z_danego_miasta(self.rejestr, miasto)
        self.widok.wyswietl_liste_pracownikow(pracownicy_z_miasta)
    
    def wyswietlanie_listy_pracownikow_wraz_z_wartoscia_dla_korporacji(self):
        lista_pracownikow = list(self.rejestr.values())
        self.widok.wyswietl_liste_wraz_z_wartososcia_dla_korporacji(lista_pracownikow)

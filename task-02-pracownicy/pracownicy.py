class AdresBudynku:
    def __init__(self, miasto, ulica, numer_budynku, numer_lokalu=None):
        self.miasto = miasto
        self.ulica = ulica
        self.numer_budynku = numer_budynku
        self.numer_lokalu = numer_lokalu
    
    def __str__(self):
        if self.numer_lokalu == None:
            return f"{{miasto: {self.miasto}, ulica: {self.ulica}, numer_budynku: {self.numer_budynku}}}"
        else:
            return f"{{miasto: {self.miasto}, ulica: {self.ulica}, numer_budynku: {self.numer_budynku}, numer_lokalu: {self.numer_lokalu}}}"

class Pracownik:
    unikalne_id = 1

    def __init__(self, imie, nazwisko, wiek, doswiadczenie, adres_budynku):
        self.id = Pracownik.unikalne_id
        Pracownik.unikalne_id += 1 
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.doswiadczenie = doswiadczenie
        self.adres_budynku = adres_budynku

    def __str__(self):
        return f"id: {self.id}, imie: {self.imie}, nazwisko: {self.nazwisko}, wiek: {self.wiek}, doswiadczenie: {self.doswiadczenie}, adres_budynku: {self.adres_budynku}"

class PracownikBiurowy(Pracownik):
    id_stanowiska = 1

    def __init__(self, imie, nazwisko, wiek, doswiadczenie, adres_budynku, intelekt):
        super().__init__(imie, nazwisko, wiek, doswiadczenie, adres_budynku)
        self.id_stanowiska = PracownikBiurowy.id_stanowiska
        PracownikBiurowy.id_stanowiska += 1 
        self.intelekt = intelekt  # 70 - 150, wyrażony w skali iq
    
    def __str__(self):
        return f"{{{super().__str__()}, id_stanowiska: {self.id_stanowiska}, intelekt: {self.intelekt}}}"
    
    def oblicz_wartosc_dla_korporacji(self):
        wartosc_dla_korporacji = self.doswiadczenie*self.intelekt
        return wartosc_dla_korporacji

class PracownikFizyczny(Pracownik):
    def __init__(self, imie, nazwisko, wiek, doswiadczenie, adres_budynku, sila_fizyczna):
        super().__init__(imie, nazwisko, wiek, doswiadczenie, adres_budynku)
        self.sila_fizyczna = sila_fizyczna # w skali: 1 - 100

    def __str__(self):
        return f"{{{super().__str__()}, sila_fizyczna: {self.sila_fizyczna}}}"
    
    def oblicz_wartosc_dla_korporacji(self):
        wartosc_dla_korporacji = self.doswiadczenie*self.sila_fizyczna/self.wiek
        return wartosc_dla_korporacji


class Handlarz(Pracownik):
    def __init__(self, imie, nazwisko, wiek, doswiadczenie, adres_budynku, skutecznosc, wysokosc_prowizji):
        super().__init__(imie, nazwisko, wiek, doswiadczenie, adres_budynku)
        self.skutecznosc = skutecznosc # NISKA ŚREDNIA lub WYSOKA
        self.wysokosc_prowizji = wysokosc_prowizji # wyrażona w %

    def __str__(self):
        return f"{{{super().__str__()}, skutecznosc: {self.skutecznosc}, wysokosc_prowizji: {self.wysokosc_prowizji}}}"
    
    def oblicz_wartosc_dla_korporacji(self):
        zamiana_skutecznosci = {"NISKA": 60, "ŚREDNIA": 90, "WYSOKA": 120}
        skutecznosc = zamiana_skutecznosci.get(self.skutecznosc)
        wartosc_dla_korporacji = self.doswiadczenie*skutecznosc
        return wartosc_dla_korporacji

from pracownicy import Pracownik, PracownikBiurowy, PracownikFizyczny, Handlarz, AdresBudynku
from rejestr import Rejestr, MetodyWspomagajaceRejestr
import unittest


class TestowanieMetodWspomagajacych(unittest.TestCase):
    
    def setUp(self):
        Pracownik.unikalne_id = 1
        self.pracownik1 = PracownikBiurowy("Jan", "Przykład", 22, 3, AdresBudynku("Gdańsk", "Gdańska", 12, 4), 99)
        self.pracownik2 = PracownikFizyczny("Grzegorz", "Fizyczny", 40, 17, AdresBudynku("Warszawa", "Krakowskie Przedmiście", 223, 15), 73)
        self.pracownik3 = Handlarz("Ignacy", "Handlowy", 54, 17, AdresBudynku("Poznań", "Legionów", 1), "WYSOKA", 18)
        self.pracownik4 = PracownikBiurowy("Jan", "Biurowy", 40, 17, AdresBudynku("Gdańsk", "Sopocka", 114, 8), 118)
        self.rejestrPracownikow = Rejestr({
            self.pracownik1.id: self.pracownik1,
            self.pracownik2.id: self.pracownik2,
            self.pracownik3.id: self.pracownik3,
            self.pracownik4.id: self.pracownik4
        })
        self.pustyRejestr = Rejestr()
        self.klasaWspomagajaca = MetodyWspomagajaceRejestr()
    
    def test_sortowanie_pracownikow_po_doswiadczeniu(self):
        expected_output = [self.pracownik4, self.pracownik2, self.pracownik3, self.pracownik1]
        posortowani_pracownicy = self.klasaWspomagajaca.posortuj_pracownikow(self.rejestrPracownikow.rejestr)
        self.assertEqual(posortowani_pracownicy, expected_output)

    def test_sortowanie_pracownikow_po_intelekcie(self):
        expected_output = [self.pracownik4, self.pracownik1, self.pracownik2, self.pracownik3]
        funkcja_sortujaca = lambda pracownik: -pracownik.intelekt
        posortowani_pracownicy = self.klasaWspomagajaca.posortuj_pracownikow(self.rejestrPracownikow.rejestr, funkcja_sortujaca)
        self.assertEqual(posortowani_pracownicy,expected_output)

    def test_sortowanie_pracownikow_pusty_rejestr(self):
        posortowani_pracownicy = self.klasaWspomagajaca.posortuj_pracownikow(self.pustyRejestr.rejestr)
        self.assertEqual(posortowani_pracownicy, [])

    def test_pracownicy_z_danego_miasta(self):
        expected_output = [self.pracownik1, self.pracownik4]
        pracownicy_z_gdanska = self.klasaWspomagajaca.wyszukaj_pracownikow_z_danego_miasta(self.rejestrPracownikow.rejestr,"Gdańsk")
        self.assertEqual(pracownicy_z_gdanska, expected_output)

    def test_pracownicy_z_danego_miasta_brak_pracownikow_z_miasta(self):
        pracownicy_z_krakowa = self.klasaWspomagajaca.wyszukaj_pracownikow_z_danego_miasta(self.rejestrPracownikow.rejestr,"Kraków")
        self.assertEqual(pracownicy_z_krakowa, [])

    def test_pracownicy_z_danego_miasta_pusty_rejestr(self):
        pracownicy_z_gdanska = self.klasaWspomagajaca.wyszukaj_pracownikow_z_danego_miasta(self.pustyRejestr.rejestr,"Gdańsk")
        self.assertEqual(pracownicy_z_gdanska, [])
    
    def test_sprawdz_klucz_float(self):
        funkcja = lambda pracownik: pracownik.doswiadczenie
        wynik = MetodyWspomagajaceRejestr.sprawdz_klucz(self.pracownik1, funkcja)
        self.assertEqual(wynik, 3)

    def test_sprawdz_klucz_str(self):
        funkcja = lambda pracownik: pracownik.imie
        wynik = MetodyWspomagajaceRejestr.sprawdz_klucz(self.pracownik1, funkcja)
        self.assertEqual(wynik, ord('J'))

    def test_sprawdz_klucz_none(self):
        funkcja = lambda pracownik: None
        wynik = MetodyWspomagajaceRejestr.sprawdz_klucz(self.pracownik1, funkcja)
        self.assertEqual(wynik, float('inf'))

    def test_sprawdz_klucz_attribute_error(self):
        funkcja = lambda pracownik: pracownik.nieistniejace_pole 
        wynik = MetodyWspomagajaceRejestr.sprawdz_klucz(self.pracownik1, funkcja)
        self.assertEqual(wynik, float('inf'))

if __name__ == '__main__':
    unittest.main()

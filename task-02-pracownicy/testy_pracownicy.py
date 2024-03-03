from pracownicy import Pracownik, PracownikBiurowy, PracownikFizyczny, Handlarz, AdresBudynku
import unittest

class TestowaniePracownika(unittest.TestCase):
    
    def setUp(self):
        Pracownik.unikalne_id = 1
        self.pracownik1 = PracownikBiurowy("Jan", "Przykład", 22, 3, AdresBudynku("Gdańsk", "Gdańska", 12, 4), 99)
        self.pracownik2 = PracownikFizyczny("Grzegorz", "Fizyczny", 40, 17, AdresBudynku("Warszawa", "Krakowskie Przedmiście", 223, 15), 73)
        self.pracownik3 = Handlarz("Ignacy", "Handlowy", 54, 17, AdresBudynku("Poznań", "Legionów", 1), "WYSOKA", 18)
        self.pracownik4 = PracownikBiurowy("Jan", "Biurowy", 40, 17, AdresBudynku("Gdańsk", "Sopocka", 114, 8), 118)

    def test_oblicz_wartosc_dla_korporacji_pracownik_biurowy(self):
        result = self.pracownik1.oblicz_wartosc_dla_korporacji()
        expected_result = self.pracownik1.doswiadczenie * self.pracownik1.intelekt 
        self.assertEqual(result, expected_result)

    def test_oblicz_wartosc_dla_korporacji_pracownik_fizyczny(self):
        result = self.pracownik2.oblicz_wartosc_dla_korporacji()
        expected_result = self.pracownik2.doswiadczenie * (self.pracownik2.sila_fizyczna / self.pracownik2.wiek)
        self.assertEqual(result, expected_result)

    def test_oblicz_wartosc_dla_korporacji_handlarz(self):
        result = self.pracownik3.oblicz_wartosc_dla_korporacji()
        zamiana_skutecznosci = {"NISKA": 60, "ŚREDNIA": 90, "WYSOKA": 120}
        skutecznosc = zamiana_skutecznosci.get(self.pracownik3.skutecznosc)
        expected_result = self.pracownik3.doswiadczenie * skutecznosc
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
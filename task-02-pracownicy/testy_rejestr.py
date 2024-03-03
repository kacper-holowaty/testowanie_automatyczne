from pracownicy import Pracownik, PracownikBiurowy, PracownikFizyczny, Handlarz, AdresBudynku
from rejestr import Rejestr, BrakPracownikaOPodanymID, PustyRejestr
import unittest
from unittest.mock import patch
import io

class TestowanieRejestru(unittest.TestCase):

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

    def test_dodaj_pracownika(self):
        self.pustyRejestr.dodaj_pracownika(self.pracownik1)
        self.assertEqual(self.pustyRejestr.rejestr[self.pracownik1.id], self.pracownik1)

    def test_usun_pracownika(self):
        expected_output = {self.pracownik1.id: self.pracownik1, self.pracownik3.id: self.pracownik3, self.pracownik4.id: self.pracownik4}
        self.rejestrPracownikow.usun_pracownika(2)
        rejestr_po_usunieciu_pracownika = self.rejestrPracownikow.rejestr
        self.assertDictEqual(rejestr_po_usunieciu_pracownika, expected_output)

    def test_usun_pracownika_pusty_rejestr(self):
        with self.assertRaises(PustyRejestr):
            self.pustyRejestr.usun_pracownika(1)
        self.assertDictEqual(self.pustyRejestr.rejestr, {})
        
    def test_usun_pracownika_brak_pracownika_o_id(self):
        expected_output = self.rejestrPracownikow.rejestr
        with self.assertRaises(BrakPracownikaOPodanymID):
            self.rejestrPracownikow.usun_pracownika(999)
        self.assertDictEqual(self.rejestrPracownikow.rejestr, expected_output)

    def test_dodaj_kilku_pracownikow(self):
        expected_output = {self.pracownik1.id: self.pracownik1, self.pracownik2.id: self.pracownik2, self.pracownik3.id: self.pracownik3, self.pracownik4.id: self.pracownik4}
        self.pustyRejestr.dodaj_kilku_pracownikow(self.pracownik1,self.pracownik2,self.pracownik3,self.pracownik4)
        self.assertDictEqual(self.pustyRejestr.rejestr, expected_output)

    def test_wyswietlanie_listy_posortowanych_pracownikow(self):
        with patch.object(Rejestr, 'wyswietlanie_listy_posortowanych_pracownikow') as mock_wyswietl:
            self.rejestrPracownikow.wyswietlanie_listy_posortowanych_pracownikow()
            mock_wyswietl.assert_called_once()

    def test_wyswietlenie_listy_pracownikow_z_danego_miasta(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.rejestrPracownikow.wyswietlanie_listy_pracownikow_z_danego_miasta("Gdańsk")
            output = mock_stdout.getvalue().strip()
            expected_output = str([str(self.pracownik1), str(self.pracownik4)])
            self.assertEqual(output, expected_output)

    def test_wyswietlenie_listy_pracownikow_wraz_z_wartoscia_dla_korporacji(self):
        with patch.object(Rejestr, 'wyswietlanie_listy_pracownikow_wraz_z_wartoscia_dla_korporacji') as mock_wyswietl:
            self.rejestrPracownikow.wyswietlanie_listy_pracownikow_wraz_z_wartoscia_dla_korporacji()
            mock_wyswietl.assert_called_once()

if __name__ == '__main__':
    unittest.main()
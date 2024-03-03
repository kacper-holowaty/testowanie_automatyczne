import unittest
from konto_bankowe import KontoBankowe, Transakcja ,BrakŚrodków
from datetime import date

class TestowanieKonto(unittest.TestCase):
    def test_wpłata(self):
        konto = KontoBankowe()
        dlugoscStartowa = len(konto.historia)
        konto.wpłata(1000, date(2023, 10, 19))
        dlugoscKoncowa = len(konto.historia)
        self.assertEqual(konto.stanKonta, 1000)
        self.assertEqual(dlugoscStartowa+1,dlugoscKoncowa)

    def test_wypłata(self):
        konto = KontoBankowe()
        dlugoscStartowa = len(konto.historia)
        konto.wpłata(3000, date(2023, 10, 19))
        konto.wypłata(2000, date(2023, 10, 19))
        dlugoscKoncowa = len(konto.historia)
        self.assertEqual(konto.stanKonta, 1000)
        self.assertEqual(dlugoscStartowa+2,dlugoscKoncowa)

    def test_wypłata_brak_środków_na_koncie(self):
        konto = KontoBankowe()
        dlugoscStartowa = len(konto.historia)
        with self.assertRaises(BrakŚrodków):
            konto.wypłata(2000, date(2023, 10, 19))
        dlugoscKoncowa = len(konto.historia)
        self.assertEqual(dlugoscStartowa, dlugoscKoncowa)

    def test_przelew(self):
        konto = KontoBankowe()
        kontoDoPrzelewu = KontoBankowe()
        dlugoscStartowa1 = len(konto.historia)
        dlugoscStartowa2 = len(kontoDoPrzelewu.historia)
        konto.wpłata(3000, date(2023, 10, 19))
        konto.przelew(2000, date(2023, 10, 19), kontoDoPrzelewu)
        dlugoscKoncowa1 = len(konto.historia)
        dlugoscKoncowa2 = len(kontoDoPrzelewu.historia)
        self.assertEqual(konto.stanKonta, 1000)
        self.assertEqual(kontoDoPrzelewu.stanKonta, 2000)
        self.assertEqual(dlugoscStartowa1 + 2, dlugoscKoncowa1)
        self.assertEqual(dlugoscStartowa2 + 1, dlugoscKoncowa2)

    def test_przelew_brak_środków_na_koncie(self):
        konto = KontoBankowe()
        kontoDoPrzelewu = KontoBankowe()
        dlugoscStartowa1 = len(konto.historia)
        dlugoscStartowa2 = len(konto.historia)
        with self.assertRaises(BrakŚrodków):
            konto.przelew(2000, date(2023, 10, 19), kontoDoPrzelewu)
        dlugoscKoncowa1 = len(konto.historia)
        dlugoscKoncowa2 = len(konto.historia)
        self.assertEqual(dlugoscStartowa1, dlugoscKoncowa1)
        self.assertEqual(dlugoscStartowa2, dlugoscKoncowa2)

    def test_wyswietl_historie(self):
        konto = KontoBankowe()
        konto.wpłata(2000, date(2023, 10, 11))
        konto.wypłata(1000, date(2023, 10, 12))
        konto.wpłata(3000, date(2023, 10, 20))
        oczekiwany_wynik = "Wpłata - Kwota: 2000, data: 2023-10-11\nWypłata - Kwota: 1000, data: 2023-10-12\n"
        self.assertEqual(konto.wyswietl_historie(date(2023, 10, 11), date(2023, 10, 19)), oczekiwany_wynik)

if __name__ == '__main__':
    unittest.main()

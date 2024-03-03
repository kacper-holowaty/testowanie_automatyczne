from pracownicy import Pracownik, PracownikBiurowy, PracownikFizyczny, Handlarz, AdresBudynku
from rejestr import Rejestr, Widok, BrakPracownikaOPodanymID, PustyRejestr

if __name__ == "__main__":
    widok = Widok()
    rejestrPracownikow = Rejestr()
    pustyRejestr = Rejestr() 
    w1 = PracownikBiurowy("Marek", "Koparek", 69, 45, AdresBudynku("Gdańsk", "Koralowa", 12, 4), 120)
    w2 = PracownikBiurowy("Jarek", "Kaczka", 34, 15, AdresBudynku("Gdańsk", "Koralowa", 12, 4), 99)
    w3 = PracownikFizyczny("Mariusz", "Pudzianowski", 44, 20, AdresBudynku("Gdańsk", "Teatralna", 69), 67)
    w4 = PracownikBiurowy("Roman", "Kosecki", 28, 5, AdresBudynku("Gdańsk", "Gwiezdna", 112, 2), 111)
    w5 = Handlarz("Mirek", "Handlarz", 58, 27, AdresBudynku("Warszawa", "Tuwima", 117, 13), "NISKA", 12)
    w6 = Handlarz("Janusz", "Cebula", 39, 20, AdresBudynku("Bydgoszcz", "Toruńska", 21, 37), "ŚREDNIA", 19)
    w7 = PracownikBiurowy("Jonasz", "Kołpak", 44, 20, AdresBudynku("Warszawa", "Słowackiego", 287, 22), 102)
    try:
        rejestrPracownikow.dodaj_pracownika(w1)
        rejestrPracownikow.dodaj_kilku_pracownikow(w2, w3, w4, w5, w6, w7)
        rejestrPracownikow.usun_pracownika(2)
    except BrakPracownikaOPodanymID:
        print("Pracownika o podanym ID nie ma w rejestrze!")
    except PustyRejestr:
        print("Rejestr jest pusty!")
    finally:
        rejestrPracownikow.wyswietlanie_listy_posortowanych_pracownikow()
        rejestrPracownikow.wyswietlanie_listy_pracownikow_z_danego_miasta("Warszawa")
        rejestrPracownikow.wyswietlanie_listy_pracownikow_wraz_z_wartoscia_dla_korporacji()
        pustyRejestr.wyswietlanie_listy_posortowanych_pracownikow()   
        rejestrPracownikow.wyswietlanie_listy_posortowanych_pracownikow(lambda pracownik: pracownik.intelekt) 
from konto_bankowe import KontoBankowe, Transakcja, BrakŚrodków
from datetime import date

if __name__ == "__main__":
    myAccount = KontoBankowe()
    differentAccount = KontoBankowe()
    try:
        myAccount.wpłata(4000, date(2023, 2, 19))
        myAccount.wpłata(1000, date(2023, 8, 21))
        myAccount.wypłata(3000, date(2023, 8, 22))
    except BrakŚrodków:
        print("Brak wystarczających środków na koncie.")
    
    try:
        myAccount.wypłata(3000, date(2023, 10, 11))
    except BrakŚrodków:
        print("Brak wystarczających środków na koncie.")
    
    try:
        myAccount.przelew(1000, date(2023, 10, 19), differentAccount)
    except BrakŚrodków:
        print("Brak wystarczających środków na koncie.")
    
    try:
        myAccount.wpłata(2500, date(2023, 11, 20))
    except BrakŚrodków:
        print("Brak wystarczających środków na koncie.")
    
    myAccount.wyswietl_historie(date(2023, 2, 20), date.today())
    differentAccount.wyswietl_historie(date(2023, 8, 31), date.today())


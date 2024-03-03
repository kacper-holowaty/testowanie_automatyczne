class BrakŚrodków(Exception):
    pass

class Transakcja:
    def __init__(self, rodzaj, kwota, data):
        self.rodzaj = rodzaj
        self.kwota = kwota
        self.data = data

class KontoBankowe:
    def __init__(self): 
        self.stanKonta = 0
        self.historia = []

    def wpłata(self, kwota, data):
        self.stanKonta += kwota
        transakcja = Transakcja("Wpłata", kwota, data)
        self.historia.append(transakcja)

    def wypłata(self, kwota, data):
        if kwota <= self.stanKonta:
            self.stanKonta = self.stanKonta - kwota
            transakcja = Transakcja("Wypłata", kwota, data)
            self.historia.append(transakcja)
        else:
            raise BrakŚrodków()
        
    def przelew(self, kwota, data, kontoDoPrzelewu):
        if kwota <= self.stanKonta:
            self.stanKonta = self.stanKonta - kwota
            kontoDoPrzelewu.stanKonta = kontoDoPrzelewu.stanKonta + kwota
            transakcja1 = Transakcja("Wykonano przelew", kwota, data)
            transakcja2 = Transakcja("Otrzymano przelew", kwota, data)
            self.historia.append(transakcja1)
            kontoDoPrzelewu.historia.append(transakcja2)
        else:
            raise BrakŚrodków()
        
    def wyswietl_historie(self, start, end):
        historiaString = ""
        for transakcja in self.historia:
            if start <= transakcja.data <= end:
                historiaString += f"{transakcja.rodzaj} - Kwota: {transakcja.kwota}, data: {transakcja.data}\n"
                print(f"{transakcja.rodzaj} - Kwota: {transakcja.kwota}, data: {transakcja.data}")
        return historiaString        
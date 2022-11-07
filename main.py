class Czlowiek:
    def __init__(self,imie,wiek):
       self.imie = imie
       self.wiek = wiek 
    
    def przedstawSie(self,powitanie = 'Cześć'):
        return powitanie +' mam na imię ' + self.imie + ' lat ' + str(self.wiek)
    
    
obiekt = Czlowiek('Sebastian', 24)
print(obiekt.imie)
print(obiekt.przedstawSie('Witam'))

obiekt2 = Czlowiek('Adrian',18)
obiekt2.imie = 'Adrian'
print(obiekt2.przedstawSie())

from math import ceil
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = 1
        
    def hello(self):
        return 'witam jestem ' + self.first_name+' '+self.last_name
    
    def go_higher(self):
        self.semester +=1
        
    def go_down(self):
        self.semester -=1
        
    def get_year(self):
        return ceil(self.semester/2)
    
janek = Student('Janko', 'Muzykant')
print('Semestr', janek.semester)    
janek.go_higher()
janek.go_higher()
print('Semestr', janek.semester)
print('Rok', janek.get_year())

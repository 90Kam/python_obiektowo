class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def hello(self):
        return 'witam jestem ' + self.first_name+' '+self.last_name
        
janek = Student('Janko','Muzykant')
print('Obiekt', janek)
print('First name is', janek.first_name)
print('Last name is', janek.last_name)

malgosia = Student('Małgosia', 'Muzykant')
print(malgosia.first_name, malgosia.last_name)
print(malgosia.hello())
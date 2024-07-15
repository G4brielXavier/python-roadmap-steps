#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Classes and DataClasses ============

#Creating a class normal of models cars

print('Normal Class')
class Info_Model:
    def __init__(self, brand, model, mph):
        self.brand = brand
        self.model = model
        self.mph = mph
        
    def __show__(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Mph: {self.mph} Mph')
    
car_one = Info_Model('Chevrolet', 'Onix LTZ', 130)
car_one.__show__()
print()

#Creating a class with DataClasses Library of models cars

from dataclasses import dataclass

print('Using DataClasses')
@dataclass
class Info_Model_New:
    brand: str
    model: str
    mph: int
    engine: str
    
    def __show__(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Mph: {self.mph} Mph')
        print(f'Engine: {self.engine}')
    
car_one = Info_Model_New('Hyundai', 'Creta', 160, 'LXC-09')
car_one.__show__()
#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Inheritance ============

class People:    
    def __init__(self, name, cpf, height):
        self.name = name
        self.cpf = cpf
        self.height = height
        
    def __show_info__(self):
        print(f'Name: {self.name}')
        print(f'CPF: {self.cpf}')
        print(f'Height: {self.height}')

class Policial(People):
    def __init__(self, dip, grade, name, cpf, height):
        self.dip = dip
        self.grade = grade
        super().__init__(name, cpf, height)
        
    def __show_info_pol__(self):
        print(f'DIP: {self.dip}')
        print(f'Grade: {self.grade}')
        
class Bombeiro(People):
    def __init__(self, bi_n, patent, name, cpf, height):
        self.bi_n = bi_n 
        self.patent = patent
        super().__init__(name, cpf, height)
        
    def __show_info_bom__(self):
        print(f'Fire Battalion: {self.bi_n}')
        print(f'Patent: {self.patent}')

pol_1 = Policial('12', 'Capitão', 'Gabriel', '292.910.012-09', 180)
bom_1 = Bombeiro('1', 'Major', 'Eduardo', '292.201.109-09', 182)


print(f'Info Policial {pol_1.name}')
print()
pol_1.__show_info__()
print()
pol_1.__show_info_pol__()
print()
print()
print(f'Info Bombeiro {bom_1.name}')
bom_1.__show_info__()
print()
bom_1.__show_info_bom__()
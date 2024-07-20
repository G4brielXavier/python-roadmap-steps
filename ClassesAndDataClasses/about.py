#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Classes and DataClasses ============

#Creating a class normal to sign-up persons

class People:
    def __init__(self, name, sobrenome, sexo, data_nascimento):
        self.name = name
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
    
    
cliente_1 = People('Gabriel', 'Xavier', 'M', '2006-05-29')

#Creating a class with DataClasses Library of sign-up persons

from dataclasses import dataclass

@dataclass
class People_class:
    name: str
    sobrenome: str
    sexo: str
    data_nascimento: str
    
cliente_plus = People_class('Dot', 'Ket', 'M', '2006/05/29')

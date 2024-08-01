#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Paradigms ============

# Programa Orientada a Objetos ( POO )

class dog:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f'{self.name} está comendo')
        
    def latir(self):
        print(f'{self.name} está latindo, au aU AU AU')
        
maillom = dog('Maillom')
belinha = dog('Belinha')

maillom.latir()
belinha.eat()



# Programação Funcional

def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
res = list(map(double, numbers))

print(res)

# Programação Procedural

def calc_area_rectangle(width, height):
    area = width * height
    return area

wid = 10
hei = 5

res = calc_area_rectangle(wid, hei)
print(res)
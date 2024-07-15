#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ RegEx - Regular Expressions ============

import re
from colorama import Fore

# search findall sub
# compile 

#Meta Caracter
# | - Ou
# . - Qualquer caracter (Com exceção do \n)
# [] - Conjunto de caracteres
# * - 0 ou n vezes
# + - 1 ou n vezes
# ? - 0 ou 1
# {n} - n quantidade de vezes que é repetido
# {min, max} - Uma range, EX: {8, 20} - De 8 a 20

#Flags
# re.I ou re.IGNORECASE - Independentemente se é maiusculo ou minusculo, ele retorna pela semelhança
# 

#Validando um CPF com Regular Expressions
#=================================
# re_default_cpf = re.compile(r'[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')

# def set_cpf(default_re):
#     re_cpf_base = None
#     cpf = ''
    
#     while re_cpf_base is None:
#         cpf = input(Fore.WHITE + 'CPF: ')
#         re_cpf_base = default_re.search(cpf)
        
#         if re_cpf_base is None:
#             print(Fore.RED + 'Formato não identificado')
        
#     return cpf
    

# res = set_cpf(re_default_cpf)
# print(Fore.GREEN + 'Formato identificado')
# ====================================

c_html = '''
<p>Phrase 1</p> <p>Phrase 2</p> <p>Phrase 3</p> <div>Phrase 4</div>
'''

print(re.findall(r'<[pdiv]{1, 3}>', c_html))
#By Gabriel Xavier - Dotket :]
#Learning Python - Backend

# ============ Inheritance ============

class Peoples:
    def __init__(self, firstname, lastname, born_date, genrer):
        self.firstname = firstname
        self.lastname = lastname
        self.born_data = born_date
        self.genrer = genrer
        
class Students(Peoples):
    def __init__(self, firstname, lastname, born_data, genrer, id_aluno, room, grade):
        self.id_aluno = id_aluno
        self.room = room
        self.grade = grade
        super().__init__(firstname, lastname, born_data, genrer)
        
student_1 = Students('Gabriel', 'Xavier', '2006-05-29', 'M', '1912-12', 10, '3th')

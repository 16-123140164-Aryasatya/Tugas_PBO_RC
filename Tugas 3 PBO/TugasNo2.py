import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Child:
    def __init__(self, father, mother):
        self.blood_type = self.waris_blood_type(father, mother)
    
    def waris_blood_type(self, father, mother):
        alel_father = random.choice(father.blood_types)
        alel_mother = random.choice(mother.blood_types)
        return alel_father + alel_mother

# Input dari pengguna
father_blood = input("Masukkan golongan darah ayah (contoh: AO, BO, AB, OO): ")
mother_blood = input("Masukkan golongan darah ibu (contoh: AO, BO, AB, OO): ")

father = Father(father_blood)
mother = Mother(mother_blood)

child = Child(father, mother)
print(f"Golongan darah anak: {child.blood_type}")

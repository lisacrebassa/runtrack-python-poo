class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom

# Instanciation d'un objet Animal
mon_animal = Animal()

# Affichage de l'âge initial
print("Âge initial de l'animal :", mon_animal.age)

# Faire vieillir l'animal
mon_animal.vieillir()
print("Âge après vieillissement :", mon_animal.age)

# Nommer l'animal
mon_animal.nommer("Rex")
print("Nom de l'animal :", mon_animal.prenom)

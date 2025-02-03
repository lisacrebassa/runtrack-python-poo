class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        print(f"Coordonées du point : ({self.x}, {self.y})")
    def afficherx(self):
        print(f"Valeur de x : {self.x}")
    def affichery(self):
        print(f"Valeur de y : {self.y}")
    def changerx(self, new_x):
        self.x = new_x
    def changery(self, new_y):
        self.y = new_y

#exemple d'utilisation
p = Point(2,3)
p.afficherLesPoints()
p.afficherx()
p.affichery()
p.changerx(10)
p.changery(20)
p.afficherLesPoints()
        
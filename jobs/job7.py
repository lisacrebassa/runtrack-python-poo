class Personnage:
    def __init__(self, x: int, y: int, taille_plateau: tuple):
        self.x = x
        self.y = y
        self.taille_plateau = taille_plateau  # (largeur, hauteur)
    
    def gauche(self):
        if self.x > 0:
            self.x -= 1
    
    def droite(self):
        if self.x < self.taille_plateau[0] - 1:
            self.x += 1
    
    def haut(self):
        if self.y > 0:
            self.y -= 1
    
    def bas(self):
        if self.y < self.taille_plateau[1] - 1:
            self.y += 1
    
    def position(self):
        return self.x, self.y

# Exemple d'utilisation
plateau = (5, 5)  # Plateau de 5x5
joueur = Personnage(2, 2, plateau)

joueur.gauche()
print(joueur.position())  # (1, 2)

joueur.haut()
print(joueur.position())  # (1, 1)

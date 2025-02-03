class Produit:
    def __init__(self, nom, prixHT, TVA):
        self._nom = nom
        self._prixHT = prixHT
        self._TVA = TVA

    def calculer_prix_TTC(self):
        return self._prixHT * (1 + self._TVA / 100)
    
    def get_nom(self):
        return self._nom
    
    def get_prixHT(self):
        return self._prixHT
    
    def get_TVA(self):
        return self._TVA
    
    def set_nom(self, nouveau_nom):
        self._nom = nouveau_nom
    
    def set_prixHT(self, nouveau_prix):
        self._prixHT = nouveau_prix
    
    def afficher(self):
        return f"Produit: {self._nom}, Prix HT: {self._prixHT}€, TVA: {self._TVA}%, Prix TTC: {self.calculer_prix_TTC()}€"

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Smartphone", 800, 20)
produit3 = Produit("Tablette", 500, 10)

# Modification des produits
produit1.set_nom("PC Portable")
produit1.set_prixHT(1200)
produit2.set_nom("iPhone")
produit2.set_prixHT(900)
produit3.set_nom("iPad")
produit3.set_prixHT(550)

# Affichage des nouveaux prix
produits = [produit1, produit2, produit3]
for produit in produits:
    print(produit.afficher())
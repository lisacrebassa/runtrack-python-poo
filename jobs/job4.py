class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom 
    def SePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

#défini les personnes avec leurs noms   
personne1=Personne('CHABRIER', 'Pierre')
personne2=Personne('LEVY', 'Sylvain')

#appelle la méthode de se présenter
print(personne1.SePresenter())
print(personne2.SePresenter())

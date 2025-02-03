class personne:
  def __init__(self , nom , prenom):
    self.nom = nom
    self.prenom = prenom
    
  def SePresenter(self):
      
      return f"je suis {self.prenom} {self.nom}"
    
personne1 = personne("Doe ", "John")
personne2 = personne("Dupond" , "Jean")

print(personne1.SePresenter())
print(personne2.SePresenter())

    
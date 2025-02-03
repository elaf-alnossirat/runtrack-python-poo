class Animal:
  def __init__(self , age = 0 , prenom = "" ):
      self.age = age
      self.prenom = prenom
      
  def AfficherAge(self):
      print(f"l'age de l'animal est {self.age} ans")  
  
  def vieillir(self):
      self.age = self.age =+ 1
      print(f"le nouveau age de l'animal est {self.age} ans ")
  
  def Nommer(self):
      self.prenom = "Luna"  
      print(f"l'animal se nomme {self.prenom}")  

animal = Animal( 0 , "")
animal.AfficherAge()
animal.vieillir()
animal.Nommer()
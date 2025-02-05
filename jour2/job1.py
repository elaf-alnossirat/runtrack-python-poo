class Rectangle:
  def __init__(self , longueur , largeur):
    self.__longueur = longueur
    self.__largeur = largeur
  
  # (getter)  
  def get_longueur(self):
      return self.__longueur
      
  def get_largeur(self):
      return self.__largeur  
    
  # (setter)  
  def set_longueur(self , nouvelle_longueur):
      if nouvelle_longueur > 0:
        self.__longueur = nouvelle_longueur
        return self.__longueur  
      else:
        print("la longueur doit etre positif!")  
    
  def set_largeur(self , nouvelle_largeur):
      if nouvelle_largeur > 0:
        self.__largeur = nouvelle_largeur
        return self.__largeur 
      else:
        print("la largeur doit etre positif!") 
        
  def afficher_infos(self):
    print(f"le rectangle est de langueur = {self.__longueur}  et de largeur = {self.__largeur} ")         
    

Rectangle = Rectangle(10 , 5)
Rectangle.afficher_infos() 

Rectangle.set_longueur(12)
Rectangle.set_largeur(6)
Rectangle.afficher_infos()   
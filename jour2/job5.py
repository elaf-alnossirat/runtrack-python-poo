class Voiture:
  def __init__(self , marque , modele , annee , kilometrage):
    self.__marque = marque
    self.__modele = modele
    self.__annee = annee
    self.__kilometrage = kilometrage
    self.__en_marche = False
    self.__reservoir = 50
    
# getters 
  def get_marque(self):
    return self.__marque
  def get_modele(self):
    return self.__modele
  def get_annee(self):
    return self.__annee
  def get_kilometrage(self):
    return self.__kilometrage
  def get_en_marche(self):
    return self.__en_marche
  def get_reservoir(self):
    return self.__reservoir
  
#setters
  def set_marque(self , marque):
    self.__marque = marque
    return self.__marque      
  def set_modele(self , modele):
    self.__modele = modele
    return self.__modele  
  def set_annee(self , annee):
    self.__annee = annee
    return self.__annee
  def set_kilometrage(self , kilometrage):
    self.__kilometrage = kilometrage
    return self.__kilometrage
  def set_en_marche(self , en_marche):
    self.__en_marche = en_marche
  def set_reservoir(self , reservoir):
    self.__reservoir = reservoir
    
  # methodes
  def __verfier_plein(self):
     return self.__reservoir 
        
    
  
  def Demarrer(self):
      if self.__verfier_plein() >= 5:
         self.__en_marche = True
         print(" la voiture est demarrée !")
      else:
         print(" Niveau de carburant insuffisant pour démarrer !") 
     
           
  def Arreter(self):
      self.__en_marche = False
      print(" La voiture est arretée !")
  
  def Afficher_info(self):
    print(f"{self.__marque} , {self.__modele} , {self.__annee} , {self.__kilometrage}")
    
car = Voiture("Tesla" , "W45" , 2022 , "250KM/H")
car.set_reservoir(3)
car.Afficher_info()
car.Demarrer() 

car.set_reservoir(40)
car.Afficher_info()
car.Demarrer()  

car.set_reservoir(40)
car.Afficher_info()
car.Arreter()  
        
            
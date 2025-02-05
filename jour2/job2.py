class Livre:
  def __init__(self , titre , auteur , pages ):
    self.__titre = titre
    self.__auteur = auteur
    self.__pages = pages
    
    
  def get_titre(self):
      return self.__titre
  def get_auteur(self):
      return self.__auteur
  def get_pages(self):
      return self.__pages 
    
  def set_titre(self , nouveau_titre):
      self.__titre = nouveau_titre
      return self.__titre
    
  def set_auteur(self , nouveau_auteur):
      self.__auteur = nouveau_auteur
      return self.__auteur
    
  def set_pages(self , nouvelles_pages):
      if nouvelles_pages > 0:
        self.__pages = nouvelles_pages
        return self.__pages
      else:
        print("erreur le nombre de pages doit étre positif")
        
  def afficher_info(self):
      print(f"les informations de ce livre : auteur : {self.__auteur},le titre : {self.__titre} ,le nombre de pages : {self.__pages}")   
      
      
livre = Livre("La Vie Simple" , "Malek Jandali" , 300) 
livre.afficher_info()

livre.set_pages(120)
livre.afficher_info() 

livre.set_pages(-80)
livre.afficher_info()          
        
        
                   
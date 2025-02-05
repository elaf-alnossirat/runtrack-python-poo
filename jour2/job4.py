class Student:
  def __init__(self , nom , prenom , numero):
    self.__nom = nom
    self.__prenom = prenom
    self.__numero = numero
    self.__credits = 0
    self.__level = self.Student_eval()
    
# method pour ajouter des credits 
  def Add_credits(self , credits):
      if credits > 0:
        self.__credits += credits
        # self.__level = self.Student_eval() 
        print(f"{credits} crédits ajoutés avec succès.")      
      else:
        print("Erreur : le nombre de crédits doit être supérieur à zéro.")
        
  # method pour afficher les credits 
  def Afficher_credits(self):
      print(f"Le nombre de credits de {self.__prenom} {self.__nom} est : {self.__credits} points")      
  
  def Student_eval(self):
      if self.__credits >= 90:
         return "Exellent" 
      elif self.__credits >= 80:
         return "Très bien"
      elif self.__credits >= 70:
        return "Bien"     
      elif self.__credits >= 60:
        return "Passable"
      else:
        return "Insuffisant"  
  
  def Afficher_infos(self):
      print(f"Nom : {self.__nom}")
      print(f"Prénom : {self.__prenom}")
      print(f"ID : {self.__numero}")
      print(f"Niveau : {self.__level}")
 
      
      

etudient = Student("John" , "Doe" , 145 )

etudient.Add_credits(15)
etudient.Add_credits(10)
etudient.Add_credits(15)

etudient.Afficher_credits()
etudient.Student_eval()

etudient.Afficher_infos()
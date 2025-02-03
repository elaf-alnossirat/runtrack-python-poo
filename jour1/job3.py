class operation:
  def __init__(self , nombre1 = 12 , nombre2 = 3):
      self.nombre1 = nombre1
      self.nombre2 = nombre2
 
 #methode pour faire l'operation de l'addition entre nombre1 et nombre2 
  def addition(self):
      resultat = self.nombre1 + self.nombre2
      print(f"le resultat de l'operation est = {resultat} ")
      
      
operation_instance = operation()
#appel de la methode addition
operation_instance.addition()



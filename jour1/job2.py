class operation:
  def __init__(self , nombre1 = 12 , nombre2 = 3):
      self.nombre1 = nombre1
      self.nombre2 = nombre2
    
  # Méthode pour afficher l'objet de manière lisible  
  def __str__(self):
     return(f"le nombre 1 est {self.nombre1}, le nombre 2 est {self.nombre2})") 
      
operation_instance = operation()

print(operation_instance)


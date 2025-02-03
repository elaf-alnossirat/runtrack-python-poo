class point:
  def __init__(self , x = 0  , y = 0 ):
    self.x = x 
    self.y = y
    
  def AficherLesPoints(self):
    print(f"les points sont {self.x} et {self.y}")

  def AfficheX(self):
    print(f" X  = {self.x}")
    
  def AfficheY(self):
    print(f" Y  = {self.y}")  
    
  def ChangerX(self , nouvel_valure_X):
      self.x = nouvel_valure_X  
      print(f"X apres changer = {self.x}")
      
  def ChangerY(self , nouvel_valure_Y):
      self.x = nouvel_valure_Y 
      print(f"Y apres changer = {self.y}")    

 
point = point(5 , 1)
point.AficherLesPoints()
point.AfficheX()
point.AfficheY()

point.ChangerX(10)
point.ChangerY(15)
  

class Personnage:
    # Constructeur de la classe
    def __init__(self, x=0, y=0):
        self.x = x  # Position horizontale (colonne)
        self.y = y  # Position verticale (ligne)

    # Méthode pour se déplacer à gauche
    def gauche(self):
        self.x -= 1
        print("Déplacement à gauche")

    # Méthode pour se déplacer à droite
    def droite(self):
        self.x += 1
        print("Déplacement à droite")

    # Méthode pour se déplacer en bas
    def bas(self):
        self.y += 1
        print("Déplacement en bas")

    # Méthode pour se déplacer en haut
    def haut(self):
        self.y -= 1
        print("Déplacement en haut")

    # Méthode pour obtenir la position actuelle sous forme de tuple
    def position(self):
        return (self.x, self.y)

# Instanciation de la classe avec une position initiale
personnage = Personnage(2, 3)

# Affichage de la position initiale
print("Position initiale :", personnage.position())

# Déplacements du personnage
personnage.gauche()  # Déplacement à gauche
print("Position après déplacement à gauche :", personnage.position())

personnage.droite()  # Déplacement à droite
print("Position après déplacement à droite :", personnage.position())

personnage.bas()     # Déplacement en bas
print("Position après déplacement en bas :", personnage.position())

personnage.haut()    # Déplacement en haut
print("Position après déplacement en haut :", personnage.position())
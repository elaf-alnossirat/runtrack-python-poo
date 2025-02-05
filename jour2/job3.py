class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True  # Attribut privé initialisé à True par défaut

    # Getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    # Setters
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
        return self.__titre

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur
        return self.__auteur

    def set_pages(self, nouvelles_pages):
        if nouvelles_pages > 0:
            self.__pages = nouvelles_pages
            return self.__pages
        else:
            print("Erreur : le nombre de pages doit être positif")

    # Méthode pour vérifier si le livre est disponible
    def vérification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.vérification():  # Vérifie si le livre est disponible
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Erreur : le livre n'est pas disponible pour emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.vérification():  # Vérifie si le livre a été emprunté
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Erreur : le livre n'a pas été emprunté.")

    # Méthode pour afficher les informations du livre
    def afficher_info(self):
        print(f"Informations du livre : Auteur : {self.__auteur}, Titre : {self.__titre}, Nombre de pages : {self.__pages}, Disponible : {self.__disponible}")


# Exemple d'utilisation
livre = Livre("La Vie Simple", "Malek Jandali", 300)
livre.afficher_info()  # Affiche les informations du livre

# Emprunter le livre
livre.emprunter()  # Le livre est emprunté
livre.afficher_info()  # Affiche les informations mises à jour

# Essayer d'emprunter à nouveau
livre.emprunter()  # Erreur : le livre n'est pas disponible

# Rendre le livre
livre.rendre()  # Le livre est rendu
livre.afficher_info()  # Affiche les informations mises à jour

# Essayer de rendre à nouveau
livre.rendre()  # Erreur : le livre n'a pas été emprunté
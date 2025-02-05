class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  # Dictionnaire contenant les plats et leurs prix
        self.__statut = "En cours"  # Par défaut, la commande est en cours

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix):
        if prix > 0:
            self.__plats[nom_plat] = prix
            print(f"✅ {nom_plat} ajouté à la commande.")
        else:
            print("❌ Erreur : Le prix du plat doit être supérieur à zéro.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        if self.__statut == "En cours":
            self.__statut = "Annulée"
            self.__plats.clear()
            print("🚫 La commande a été annulée.")
        else:
            print("❌ La commande ne peut plus être annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        return sum(self.__plats.values())

    # Méthode pour afficher la commande avec son total
    def afficher_commande(self):
        print(f"\n🧾 Commande n°{self.__numero_commande} - Statut : {self.__statut}")
        if self.__plats:
            for plat, prix in self.__plats.items():
                print(f"🍽️ {plat} - {prix:.2f}€")
            total = self.__calculer_total()
            print(f"💰 Total à payer : {total:.2f}€ (Hors TVA)")
            print(f"💵 Total avec TVA (20%) : {self.calculer_tva():.2f}€")
        else:
            print("Aucun plat dans la commande.")

    # Méthode pour calculer le total avec la TVA (20%)
    def calculer_tva(self):
        total = self.__calculer_total()
        return total * 1.2  # Ajoute 20% de TVA

    # Méthode pour terminer la commande
    def terminer_commande(self):
        if self.__statut == "En cours":
            self.__statut = "Terminée"
            print("✅ La commande a été terminée.")
        else:
            print("❌ La commande ne peut pas être modifiée.")

# Exemple d'utilisation
commande1 = Commande(101)

commande1.ajouter_plat("Pizza Margherita", 12.50)
commande1.ajouter_plat("Pâtes Carbonara", 14.00)
commande1.ajouter_plat("Tiramisu", 6.50)

commande1.afficher_commande()

# Terminer la commande
commande1.terminer_commande()
commande1.afficher_commande()

# Essayer d'annuler après avoir terminé
commande1.annuler_commande()

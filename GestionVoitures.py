class voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        Self.couleur = couleur

    def afficherInformations(self):
        print("Matricule:" , self.matricule)
        print("Marque:" , self.marque)
        print("Couleur:" , self.couleur)

class Parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = ()

    def entrerVoiture(self, voiture):

        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                print("La voiture existe déjà dans le parc.")
                return

            if len(self.listeVoitures) < self.capacite:
                self.listeVoitures.apprend(voiture)
                print("Voiture ajoutée au parc.")
            else:
                print("Le parc est plein.")

    def sortirVoiture(self, voiture):

        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                self.listeVoitures.remove(v)
                print("Voiture retiréé du parc.")
                print("Places libres :", self.calculerNombrePlacesLibres())
                return

            print("La voiture n'est pas dans le parc.")
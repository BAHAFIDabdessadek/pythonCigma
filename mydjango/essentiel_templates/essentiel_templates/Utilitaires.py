class Etudiant:
    def __init__(self, matricule, nom, prenom, genre, note):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.note = note
    def nomcomplet(self):
        return self.nom +" "+self.prenom

    def genre_entier(self):
        if self.genre == "M":
            return "Masculin"
        else:
            return "Feminin"

    def mention(self):
        if self.note >= 16 :
            return "Tres Bien"
        if self.note >= 14 :
            return "Bien"
        if self.note >= 12 :
            return "assez Bien"
        if self.note >=10:
            return "passable"
        else:
            return "Non admis"



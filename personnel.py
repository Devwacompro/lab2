class Personne:
    nom = 0
    prenom = 0
    dateNaissance = 0
    
    def __init__(self, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
    
    def set_nom(self, nom):
        self.nom = nom
        
    def get_nom(self):
        return self.nom
        
    def set_prenom(self, prenom):
        self.prenom = prenom
    
    def get_prenom(self):
        return self.prenom
    
    def set_dateNaissance(self, dateNaissance):
        self.dateNaissance = dateNaissance
    
    def get_dateNaissance(self):
        return self.dateNaissance
    
    def __str__(self):
        return "La personne:"+ str(self.get_prenom()) + " " + str(self.get_nom())+ " "  + "est née le" + " " + str(self.get_dateNaissance())
    
    
class Etudiant (Personne):
    matricule = -999
    cours = {}
    moyenne = -999
    dateInscription = 0
    
    def __init__(self, nom, prenom, dateNaissance, matricule, cours, dateInscription):
        Personne.__init__(self, nom, prenom, dateNaissance)
        matSize = str(matricule)
        if len(matSize) != 8:
            raise TypeError("La matricule doit être un numéro à 8 chiffres")                   
        if not isinstance(cours, dict):
             raise TypeError("Les cours doivent être un dictionnaire")
            
        self.matricule = matricule
        self.cours = cours
        for value in cours.values():
            self.moyenne += value
        try: 
            self.moyenne = self.moyenne/len(cours)
        except ZeroDivisionError:
            self.moyenne = "Division par Zéro"
            
        self.dateInscription = dateInscription
        
        
    def set_matricule(self, matricule):
        self.matricule = matricule
        
    def get_matricule(self):
        return self.matricule
    
    def set_cours(self, cours):
        self.cours = cours
        
    def get_cours(self):
        return self.cours
    
    def set_moyenne(self, moyenne):
        self.moyenne = moyenne
        
    def get_moyenne(self):
        return self.moyenne
    
    def set_dateInscription(self, dateInscription):
        self.dateInscription = dateInscription
        
    def get_dateInscription(self):
        return self.dateInscription
    
    def __str__(self):
        return super(Etudiant, self).__str__()+ "\n"+"Et est un étudiant avec la matricule :" + str(self.get_matricule()) + "\n" + "Sa moyenne est:" + str(self.get_moyenne()) + "\n" +"Sa date d'inscription au programme est :" + str(self.get_dateInscription()) + "\n" + "Et est inscrit aux cours:" +  str(self.get_cours)
        for key in self.cours:
            print(key, ' : ', self.cours.get(key))
    
    
class Professeur (Personne):
    diplome = 0
    specialite = 0
    
    def __init__(self, nom, prenom, dateNaissance, diplome, specialite):
        Personne.__init__(self, nom, prenom, dateNaissance)
        self.diplome = diplome
        self.specialite = specialite
    
    def set_diplome(self, diplome):
        self.diplome = diplome
        
    def get_diplome(self):
        return self.diplome
    
    def set_specialite(self, specialite):
        self.specialite = specialite
        
    def get_specialite(self):
        return self.specialite
    
    def printProfesseur (self):
        Personne.printPersonne(self)
        print("Et est un professeur avec le diplôme :", self.diplome)
        print("Et sa spécialité est :", self.specialite)
    

print("Personne=====================================")
p1 = Personne("Beaulieu", "Dèvick", "2000-09-22")
print(p1)

#print("Etudiant=====================================")
#cours = {"10324": 80, "41935": 70, "58305" : 75}


#e1 = Etudiant("Beaulieu", "Dèvick", "2000-09-22", 20001030, cours, "2020-10-09")
#e1.printEtudiant()

#print("Etudiant Exception=====================================")
#cours = {}

#e1 = Etudiant("Beaulieu", "Dèvick", "2000-09-22", 20001030, cours, "2020-10-09")
#e1.printEtudiant()

#print("Professeur Exception=====================================")
#prof1 = Professeur("Andrée", "Marc", "1990-05-12", "DEC en TI", "Base donnée")
#prof1.printProfesseur()
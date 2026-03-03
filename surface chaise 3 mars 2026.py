
class Chaise():
    def __init__(self): # fonction qui va demarre des quon appelle la classe
        
        self.materiaux="" #ou alors tu peux mettre srt ce qui veut aussi dire string
        self.prix= float()
        self.hauteur=float()
        self.largeur=float() # int veut dire on veut une valeur d'un nombre entier
        self.profondeur=float() # self c'est quand on partle des differente variable depuis l'interieure de la classe
        self.couleur=""
        self.poids=float()
        self.surface=float() # avec float je peux mettre comme valeur un nombre qui n'est pas entier 
       
    def calc_surface (self):
        self.surface=self.profondeur*self.largeur

chaise=Chaise() # instanciation de la classe chaise
#nombre_1=int #ca vezut direz cree une variable qui s'appelle nombre 1 et  qui est du type integer

chaise.materiaux="bois"
chaise.prix=160
chaise.hauteur=0.8
chaise.profondeur=0.5
chaise.largeur=0.4

chaise.calc_surface()
   

print(chaise.surface)

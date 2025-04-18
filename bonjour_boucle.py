print("Bonjour et bienvenue dans ce programme qui vous dit bonjour")



choix="o"

while choix == "o":
  print("Bonjour")
  choix=input("voulez vous continuer?")
  while choix not in ["n","o"]:
    choix = input("Veuillez répondre par oui (o) ou non (n)")

print( "Au revoir !")

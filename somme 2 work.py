import random 

nombre1 = random.randint(-100,100)
nombre2 = random.randint(-100,100)

somme = nombre1 + nombre2

question="Que vaut la somme de " +str (nombre1)+ " et "+str(nombre2)+ "?"
reponse = input(question)

while valid ==0:
  try:
    reponse=int(reponse)
  except:
    print("Votre réponse n'est pas un nombre entier")
    reponse=input("Quelle est votre réponse?")

if reponse==somme:
   print ("Bien vu ;) !")

elif reponse != somme:
    print ("Imbécile :( !!")
    print("recommence")

else :
    print("Y a beuggggggggg")

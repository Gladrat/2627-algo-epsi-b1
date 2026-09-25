# collection ordonnées de 0 à n éléments représentés par leur indice

notes_b1 = []
saisie = True

while saisie:
    nouvelle_note = int(input("Quelle est la note de l'élève ? "))
    notes_b1.append(nouvelle_note)
    print("Voulez-vous saisir une nouvelle note ? (o/n) ")
    reponse = input("Votre choix : ")
    if reponse != "o":
        saisie = False

def calculer_moyenne(notes_dune_classe):
    total = 0
    for n in notes_dune_classe:
        total = total + n
    return total / len(notes_b1)

moy = calculer_moyenne(notes_b1)
print("La moyenne de la classe est :", moy)
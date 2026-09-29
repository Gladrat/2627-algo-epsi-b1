# collection ordonnées de 0 à n éléments représentés par leur indice

tab = [10, 12, 13]
tab.append(18)

print(tab)

for i in tab:
    print(i)

word = "ALGORITHMIE"
lettre = word[7]

for lettre in word[::-1]:
    print(lettre)

print(lettre)

notes_b1 = []
saisie = True

grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["H", "I", "J"],
]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        print("Ligne:", row, "Colonne:", col, "Valeur:", grid[row][col])

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
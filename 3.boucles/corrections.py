# Exercice 1

total = 0

for i in range(1, 13):
    if i % 4 == 0:
        total += 8
        print("Sauvegarde complète : 8s")
    else:
        total += 2
        print("Sauvegarde incrémentale : 2s")

print("Temps total :", total, "s")

# Exercice 2

remaining = int(input("Combien de Mo à télécharger ? "))
seconds = 0
chunk = 0

while remaining > 0:

    if remaining > 300:
        chunk = 120
    else:
        chunk = 70

    if chunk > remaining:
        chunk = remaining

    remaining = remaining - chunk
    seconds = seconds + 1

    print(seconds)
    print(remaining)

print(seconds)
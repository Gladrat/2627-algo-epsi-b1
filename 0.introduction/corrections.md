# Exercice facile - Le billet de concert

Objectif : On cherche le prix total de commande

Entrées :
- nombre de places : 3
- prix d'une place : 32 €
- frais fixes : 2,50 €
- frais de service : 5 % du prix des places

Algorithme :
1. Demander le nombre de places
2. Calculer le prix total des places
3. Calculer 5% de ce prix
4. Ajouter les frais de service et les frais fixes
5. Afficher le total

Pseudo-code:
```ascii
prix_place = nombre_places * prix_unitaire
frais_service = prix_place * taux_service
total = prix_place + frais_service + frais fixes
```

procedure calcul_billet:

end procedure_billet;

# Exercice difficile - Livraison de batteries

Entrées :

- poids d'une batterie : **430 g** ;
- charge maximale du drone : **2 500 g** ;
- nombre de batteries : **17**.

Résultat attendu :

- nombre total de trajets.

Résultats intermédiaires utiles :

- capacité maximale d'un trajet ;
- nombre de trajets complets ;
- nombre de batteries restantes.

## La démarche

La division entière permet de savoir combien de batteries de 430 g tiennent dans 2 500 g :

```
2500 // 430 = 5
```

Le drone peut donc transporter **5 batteries** au maximum par trajet.

Vérification :

```
5 × 430 = 2150 g
6 × 430 = 2580 g
```

Six batteries dépasseraient la limite.

On peut ensuite décomposer les 17 batteries en groupes de 5 :

```
17 // 5 = 3
17 % 5 = 2
```

On a donc :

- **3 trajets complets** de 5 batteries ;
- **2 batteries restantes**.

Il faut alors un quatrième trajet.

## Résultat de l'exercice

On peut donc écrire :

```
trajets complets = 3
batteries restantes = 2
donc trajets au total = 3 + 1 = 4
```

## En Python

```python
battery_weight = 430
max_payload = 2500
battery_count = 17

batteries_per_trip = max_payload // battery_weight
full_trips = battery_count // batteries_per_trip
remaining_batteries = battery_count % batteries_per_trip
total_trips = full_trips + 1

print("batteries par trajet :", batteries_per_trip)
print("trajets complets :", full_trips)
print("batteries restantes :", remaining_batteries)
print("trajets au total :", total_trips)
```
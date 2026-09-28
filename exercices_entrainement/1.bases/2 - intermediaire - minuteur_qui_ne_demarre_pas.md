# Un minuteur qui ne démarre pas

**Niveau :** intermédiaire  
**Format :** correction de bug

Le programme suivant doit convertir une durée saisie en secondes en minutes et secondes :

```python
raw_seconds = input("Durée en secondes : ")

minutes = raw_seconds // 60
seconds = raw_seconds % 60

print(minutes, seconds)
```

Le programme échoue avant d'afficher le résultat.

1. Identifiez la cause.
2. Corrigez le programme.
3. Expliquez pourquoi la conversion doit avoir lieu avant les calculs.

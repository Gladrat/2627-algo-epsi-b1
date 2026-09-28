# Mode économie

**Niveau :** base  
**Format :** lecture de code

Sans exécuter :

```python
battery = 28
is_charging = False

if battery < 20:
    print("critique")
elif battery < 40 and not is_charging:
    print("économie")
else:
    print("normal")
```

1. Quel texte est affiché ?
2. Quelle condition est réellement vraie ?
3. Pourquoi le `else` n'est-il pas exécuté ?

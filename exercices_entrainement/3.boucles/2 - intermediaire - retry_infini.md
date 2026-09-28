# Le retry infini

**Niveau :** intermédiaire  
**Format :** correction de bug

> **Contexte :** lorsqu'une opération échoue, un programme peut essayer de nouveau automatiquement. Une nouvelle tentative est souvent appelée un **retry**. Ici, on veut simplement limiter ce mécanisme à trois tentatives.

Ce programme doit effectuer au maximum trois tentatives :

```python
attempt = 1

while attempt <= 3:
    print("tentative", attempt)
```

1. Pourquoi la boucle ne se termine-t-elle jamais ?
2. Quelle information représente `attempt` ?
3. Corrigez le programme pour afficher exactement trois tentatives.

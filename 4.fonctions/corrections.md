# Exercice — Limiter un volume

**Le contrat :** La fonction reçoit un volume et doit toujours renvoyer une valeur comprise entre 0 et 100.

1. Volume < 0 → Renvoyer 0
2. Volume > 100 → Renvoyer 100
3. Dans tous les autres cas → Renvoyer le volume reçu

```ascii
si volume < 0
  renvoyer 0

si volume > 100
  renvoyer 100

renvoyer volume
```
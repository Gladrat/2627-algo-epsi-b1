# Construire une nouvelle liste

**Niveau :** base  
**Format :** lecture de code

Sans exécuter :

```python
services = ["api", "web", "db"]
labels = []

for service in services:
    labels.append(service.upper())

services[0] = "worker"

print(services)
print(labels)
```

1. Quel est le contenu final de `services` ?
2. Quel est le contenu final de `labels` ?
3. Pourquoi la modification de `services[0]` ne change-t-elle pas le premier élément de `labels` ?

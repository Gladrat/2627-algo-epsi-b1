# Découper un bloc de données

**Niveau :** intermédiaire  
**Format :** lecture de code

Sans exécuter :

```python
data_size = 1547
block_size = 512

full_blocks = data_size // block_size
remaining = data_size % block_size

print(full_blocks, remaining)
```

1. Quelles valeurs sont affichées ?
2. Que représente concrètement `full_blocks` ?
3. Que représente `remaining` ?
4. Faites une petite trace des deux calculs.

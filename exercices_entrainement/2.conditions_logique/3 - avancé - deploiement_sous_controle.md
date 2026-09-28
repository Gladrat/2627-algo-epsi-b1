# Déploiement sous contrôle

**Niveau :** avancé  
**Format :** conception

> **Contexte :** une équipe s'apprête à publier une nouvelle version de son application. Une **branche** représente ici une version de travail du projet et `"main"` désigne la version principale. Un **gel de déploiement** interdit temporairement les publications. Un **hotfix** est une correction urgente qui peut exceptionnellement être publiée pendant ce gel. Il n'est pas nécessaire de connaître Git pour résoudre l'exercice.

Un déploiement est autorisé normalement si :

- les tests passent ;
- la branche est `"main"` ;
- aucun gel de déploiement n'est actif.

Exception : un **hotfix sur la branche `"main"`** peut être déployé pendant un gel si les tests passent et si la personne est administratrice.

On dispose de :

```python
tests_passed = True
branch = "main"
is_freeze = True
is_hotfix = True
is_admin = True
```

Construisez un booléen `can_deploy`, puis affichez `"déploiement"` ou `"bloqué"`.

Avant de coder, séparez clairement le **cas normal** et le **cas d'exception**.

Testez au moins trois situations différentes.

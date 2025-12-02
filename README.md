# Gestionnaire de Tâches

Un programme Python simple pour gérer votre liste de tâches.

## Fonctionnalités

- ✅ Ajouter une tâche (avec date/heure de création)
- ✅ Afficher les tâches avec leur statut (○ en cours, ✓ complétée)
- ✅ Marquer une tâche comme complétée (historique conservé)
- ✅ Supprimer une tâche
- ✅ Sauvegarder dans une base de données SQLite

## Comment utiliser

### Version en ligne de commande
```bash
python main.py
```

### Version avec interface graphique (GUI)
```bash
python gui.py
```

#### Options du menu en ligne de commande:
   - **1**: Ajouter une tâche
   - **2**: Afficher vos tâches
   - **3**: Marquer une tâche comme complétée
   - **4**: Supprimer une tâche
   - **5**: Quitter

#### Boutons de la GUI:
   - **Ajouter**: Ajoute une nouvelle tâche
   - **Marquer comme complétée**: Marque la tâche sélectionnée comme complétée
   - **Supprimer**: Supprime la tâche sélectionnée
   - **Actualiser**: Actualise la liste des tâches

## Fichiers

- `main.py`: Le programme en ligne de commande
- `gui.py`: Le programme avec interface graphique
- `taches.db`: Base de données SQLite (créée automatiquement)

## Améliorations futures possibles

Ces améliorations pourraient être implémentées après maîtrise des bases:

1. **Ajouter des dates/heures** aux tâches
   - Utiliser le module `datetime`
   - Afficher quand chaque tâche a été créée

2. **Marquer les tâches comme "complétées"** au lieu de les supprimer
   - Garder un historique des tâches
   - Afficher un statut (✓ complétée, ○ en cours)

3. ~~**Utiliser une base de données** au lieu d'un fichier txt~~
   - ~~Découvrir SQLite (plus robuste qu'un fichier)~~
   - ~~Meilleure gestion des données~~
   - ✅ **COMPLÉTÉE**: Utilisation de SQLite!

4. ~~**Ajouter une interface graphique (GUI)**~~
   - ~~Utiliser tkinter (bibliothèque Python)~~
   - ~~Plus convivial qu'une interface en ligne de commande~~
   - ✅ **COMPLÉTÉE**: Interface graphique avec tkinter!

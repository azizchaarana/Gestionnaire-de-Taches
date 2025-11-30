# Gestionnaire de Tâches

Un programme Python simple pour gérer votre liste de tâches.

## Fonctionnalités

- ✅ Ajouter une tâche (avec date/heure de création)
- ✅ Afficher les tâches avec leur statut (○ en cours, ✓ complétée)
- ✅ Marquer une tâche comme complétée (historique conservé)
- ✅ Supprimer une tâche
- ✅ Sauvegarder automatiquement dans un fichier

## Comment utiliser

1. Lancez le programme:
```bash
python main.py
```

2. Choisissez une option du menu:
   - **1**: Ajouter une tâche
   - **2**: Afficher vos tâches
   - **3**: Marquer une tâche comme complétée
   - **4**: Supprimer une tâche
   - **5**: Quitter

## Fichiers

- `main.py`: Le programme principal
- `taches.txt`: Fichier où les tâches sont sauvegardées (créé automatiquement)

## Améliorations futures possibles

Ces améliorations pourraient être implémentées après maîtrise des bases:

1. **Ajouter des dates/heures** aux tâches
   - Utiliser le module `datetime`
   - Afficher quand chaque tâche a été créée

2. **Marquer les tâches comme "complétées"** au lieu de les supprimer
   - Garder un historique des tâches
   - Afficher un statut (✓ complétée, ○ en cours)

3. **Utiliser une base de données** au lieu d'un fichier txt
   - Découvrir SQLite (plus robuste qu'un fichier)
   - Meilleure gestion des données

4. **Ajouter une interface graphique (GUI)**
   - Utiliser tkinter (bibliothèque Python)
   - Plus convivial qu'une interface en ligne de commande

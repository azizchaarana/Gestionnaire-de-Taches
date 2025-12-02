# Gestionnaire de Tâches Simple
# Pour débuter en Python

import sqlite3
from datetime import datetime

def afficher_menu():
    print("\n=== GESTIONNAIRE DE TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme complétée")
    print("4. Supprimer une tâche")
    print("5. Quitter")
    choix = input("\nChoisissez une option (1-5): ")
    return choix


def initialiser_base_donnees():
    """Crée la base de données et la table si elles n'existent pas"""
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS taches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            statut TEXT NOT NULL,
            date_creation TEXT NOT NULL
        )
    """)
    connexion.commit()
    connexion.close()


def charger_taches():
    """Charge les tâches depuis la base de données"""
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT id, description, statut FROM taches")
    resultats = curseur.fetchall()
    connexion.close()

    taches = []
    for id, description, statut in resultats:
        taches.append({
            "id": id,
            "description": description,
            "statut": statut
        })
    return taches


def sauvegarder_tache(description, statut="en cours"):
    """Ajoute une nouvelle tâche dans la base de données"""
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    date_creation = datetime.now().strftime("%d/%m/%Y %H:%M")
    curseur.execute(
        "INSERT INTO taches (description, statut, date_creation) VALUES (?, ?, ?)",
        (description, statut, date_creation)
    )
    connexion.commit()
    connexion.close()


def mettre_a_jour_statut(id_tache, nouveau_statut):
    """Met à jour le statut d'une tâche"""
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE taches SET statut = ? WHERE id = ?", (nouveau_statut, id_tache))
    connexion.commit()
    connexion.close()


def supprimer_tache_db(id_tache):
    """Supprime une tâche de la base de données"""
    connexion = sqlite3.connect("taches.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM taches WHERE id = ?", (id_tache,))
    connexion.commit()
    connexion.close()


def ajouter_tache(taches):
    """Ajoute une nouvelle tâche avec la date/heure actuelle"""
    tache = input("Entrez la tâche: ")
    if tache:
        sauvegarder_tache(tache)
        print("✓ Tâche ajoutée!")
    else:
        print("✗ Tâche vide, non ajoutée")


def afficher_taches(taches):
    """Affiche toutes les tâches avec leur statut"""
    if not taches:
        print("\nAucune tâche pour le moment!")
    else:
        print("\n=== VOS TÂCHES ===")
        for i, tache in enumerate(taches, 1):
            icone = "✓" if tache["statut"] == "complétée" else "○"
            print(f"{i}. [{icone}] {tache['description']} (ID: {tache['id']})")


def marquer_completee(taches):
    """Marque une tâche comme complétée"""
    afficher_taches(taches)

    if not taches:
        return

    try:
        numero = int(input("\nNuméro de la tâche à marquer comme complétée: "))
        if 1 <= numero <= len(taches):
            tache = taches[numero - 1]
            mettre_a_jour_statut(tache["id"], "complétée")
            print(f"✓ Tâche '{tache['description']}' marquée comme complétée!")
        else:
            print("✗ Numéro invalide")
    except ValueError:
        print("✗ Veuillez entrer un nombre")


def supprimer_tache(taches):
    """Supprime une tâche"""
    afficher_taches(taches)

    if not taches:
        return

    try:
        numero = int(input("\nNuméro de la tâche à supprimer: "))
        if 1 <= numero <= len(taches):
            tache = taches[numero - 1]
            supprimer_tache_db(tache["id"])
            print(f"✓ Tâche '{tache['description']}' supprimée!")
        else:
            print("✗ Numéro invalide")
    except ValueError:
        print("✗ Veuillez entrer un nombre")


def main():
    print("Bienvenue dans le Gestionnaire de Tâches!")
    initialiser_base_donnees()

    while True:
        taches = charger_taches()
        choix = afficher_menu()

        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            afficher_taches(taches)
        elif choix == "3":
            marquer_completee(taches)
        elif choix == "4":
            supprimer_tache(taches)
        elif choix == "5":
            print("\nAu revoir! 👋")
            break
        else:
            print("✗ Option invalide")


if __name__ == "__main__":
    main()

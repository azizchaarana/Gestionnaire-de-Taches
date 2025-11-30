# Gestionnaire de Tâches Simple
# Pour débuter en Python

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


def charger_taches():
    """Charge les tâches depuis le fichier"""
    try:
        with open("taches.txt", "r") as fichier:
            taches = []
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    # Format: description | statut
                    if " | statut:" in ligne:
                        parts = ligne.rsplit(" | statut:", 1)
                        taches.append({
                            "description": parts[0],
                            "statut": parts[1]
                        })
                    else:
                        # Format ancien (compatibilité)
                        taches.append({
                            "description": ligne,
                            "statut": "en cours"
                        })
            return taches
    except FileNotFoundError:
        return []


def sauvegarder_taches(taches):
    """Sauvegarde les tâches dans le fichier"""
    with open("taches.txt", "w") as fichier:
        for tache in taches:
            description = tache["description"]
            statut = tache["statut"]
            fichier.write(f"{description} | statut:{statut}\n")


def ajouter_tache(taches):
    """Ajoute une nouvelle tâche avec la date/heure actuelle"""
    tache = input("Entrez la tâche: ")
    if tache:
        # Ajouter la date et l'heure actuelles
        date_heure = datetime.now().strftime("%d/%m/%Y %H:%M")
        description = f"{tache} | Créée le: {date_heure}"
        taches.append({
            "description": description,
            "statut": "en cours"
        })
        sauvegarder_taches(taches)
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
            print(f"{i}. [{icone}] {tache['description']}")


def marquer_completee(taches):
    """Marque une tâche comme complétée"""
    afficher_taches(taches)

    if not taches:
        return

    try:
        numero = int(input("\nNuméro de la tâche à marquer comme complétée: "))
        if 1 <= numero <= len(taches):
            taches[numero - 1]["statut"] = "complétée"
            sauvegarder_taches(taches)
            print(f"✓ Tâche '{taches[numero - 1]['description']}' marquée comme complétée!")
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
            tache_supprimee = taches.pop(numero - 1)
            sauvegarder_taches(taches)
            print(f"✓ Tâche '{tache_supprimee['description']}' supprimée!")
        else:
            print("✗ Numéro invalide")
    except ValueError:
        print("✗ Veuillez entrer un nombre")


def main():
    print("Bienvenue dans le Gestionnaire de Tâches!")
    taches = charger_taches()

    while True:
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

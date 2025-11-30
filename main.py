# Gestionnaire de Tâches Simple
# Pour débuter en Python

def afficher_menu():
    print("\n=== GESTIONNAIRE DE TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")
    choix = input("\nChoisissez une option (1-4): ")
    return choix


def charger_taches():
    """Charge les tâches depuis le fichier"""
    try:
        with open("taches.txt", "r") as fichier:
            taches = fichier.read().strip().split("\n")
            return [t for t in taches if t]  # Supprimer les lignes vides
    except FileNotFoundError:
        return []


def sauvegarder_taches(taches):
    """Sauvegarde les tâches dans le fichier"""
    with open("taches.txt", "w") as fichier:
        for tache in taches:
            fichier.write(tache + "\n")


def ajouter_tache(taches):
    """Ajoute une nouvelle tâche"""
    tache = input("Entrez la tâche: ")
    if tache:
        taches.append(tache)
        sauvegarder_taches(taches)
        print("✓ Tâche ajoutée!")
    else:
        print("✗ Tâche vide, non ajoutée")


def afficher_taches(taches):
    """Affiche toutes les tâches"""
    if not taches:
        print("\nAucune tâche pour le moment!")
    else:
        print("\n=== VOS TÂCHES ===")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")


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
            print(f"✓ Tâche '{tache_supprimee}' supprimée!")
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
            supprimer_tache(taches)
        elif choix == "4":
            print("\nAu revoir! 👋")
            break
        else:
            print("✗ Option invalide")


if __name__ == "__main__":
    main()

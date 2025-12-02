# Interface Graphique - Gestionnaire de Tâches
# Utilise tkinter pour une interface conviviale

import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3
from datetime import datetime

# Fonctions de base de données (même que dans main.py)
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


class GestionnaireTachesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire de Tâches")
        self.root.geometry("600x500")
        self.tache_selectionnee = None

        initialiser_base_donnees()

        # Frame pour l'entrée de nouvelle tâche
        frame_entree = tk.Frame(root, bg="#f0f0f0", pady=10)
        frame_entree.pack(fill=tk.X)

        tk.Label(frame_entree, text="Nouvelle tâche:", bg="#f0f0f0", font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        self.entry_tache = tk.Entry(frame_entree, width=40, font=("Arial", 10))
        self.entry_tache.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_entree, text="Ajouter", command=self.ajouter_tache, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

        # Frame pour la liste des tâches
        frame_liste = tk.Frame(root)
        frame_liste.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(frame_liste, text="Vos Tâches:", font=("Arial", 12, "bold")).pack(anchor=tk.W)

        # Listbox pour afficher les tâches
        self.listbox = tk.Listbox(frame_liste, font=("Arial", 10), height=15)
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.on_tache_selectionnee)

        # Frame pour les boutons d'action
        frame_boutons = tk.Frame(root, bg="#f0f0f0", pady=10)
        frame_boutons.pack(fill=tk.X)

        tk.Button(frame_boutons, text="Marquer comme complétée", command=self.marquer_completee, bg="#2196F3", fg="white", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_boutons, text="Supprimer", command=self.supprimer_tache, bg="#f44336", fg="white", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_boutons, text="Actualiser", command=self.actualiser_liste, bg="#FF9800", fg="white", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)

        self.actualiser_liste()

    def actualiser_liste(self):
        """Actualise l'affichage de la liste des tâches"""
        self.listbox.delete(0, tk.END)
        taches = charger_taches()

        for tache in taches:
            icone = "✓" if tache["statut"] == "complétée" else "○"
            affichage = f"[{icone}] {tache['description']} (ID: {tache['id']})"
            self.listbox.insert(tk.END, affichage)

        self.taches = taches

    def on_tache_selectionnee(self, event):
        """Appelé quand une tâche est sélectionnée"""
        selection = self.listbox.curselection()
        if selection:
            self.tache_selectionnee = selection[0]

    def ajouter_tache(self):
        """Ajoute une nouvelle tâche"""
        description = self.entry_tache.get()

        if not description.strip():
            messagebox.showwarning("Avertissement", "Veuillez entrer une tâche!")
            return

        sauvegarder_tache(description)
        self.entry_tache.delete(0, tk.END)
        messagebox.showinfo("Succès", "Tâche ajoutée!")
        self.actualiser_liste()

    def marquer_completee(self):
        """Marque la tâche sélectionnée comme complétée"""
        if self.tache_selectionnee is None:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une tâche!")
            return

        tache = self.taches[self.tache_selectionnee]
        mettre_a_jour_statut(tache["id"], "complétée")
        messagebox.showinfo("Succès", f"Tâche '{tache['description']}' marquée comme complétée!")
        self.actualiser_liste()

    def supprimer_tache(self):
        """Supprime la tâche sélectionnée"""
        if self.tache_selectionnee is None:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner une tâche!")
            return

        tache = self.taches[self.tache_selectionnee]
        if messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer:\n'{tache['description']}'?"):
            supprimer_tache_db(tache["id"])
            messagebox.showinfo("Succès", "Tâche supprimée!")
            self.actualiser_liste()


def main():
    root = tk.Tk()
    app = GestionnaireTachesGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

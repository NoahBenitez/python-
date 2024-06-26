tasks = [
    {"nom": "Faire les devoirs", "description": "Mathématiques et français", "date_d_echeance": "2023-12-10", "etat": "en cours"},
    {"nom": "Réviser Python", "description": "Préparation pour l'examen", "date_d_echeance": "2023-12-15", "etat": "en attente"}
]

def afficher_taches():
    print("\nListe des tâches:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task['nom']} - {task['description']} - Date d'échéance: {task['date_d_echeance']} - État: {task['etat']}")

def ajouter_tache():
    nom = input("Nom de la tâche : ")
    description = input("Description de la tâche : ")
    date_d_echeance = input("Date d'échéance (format YYYY-MM-DD) : ")
    etat = input("État de la tâche (en cours, terminée, en attente) : ")

    nouvelle_tache = {
        "nom": nom,
        "description": description,
        "date_d_echeance": date_d_echeance,
        "etat": etat
    }

    tasks.append(nouvelle_tache)
    print("Tâche ajoutée avec succès!")

def mettre_a_jour_tache():
    afficher_taches()
    choix = int(input("Choisissez le numéro de la tâche à mettre à jour : ")) - 1

    if 0 <= choix < len(tasks):
        task = tasks[choix]
        print(f"Tâche actuelle : {task['nom']} - {task['description']} - Date d'échéance: {task['date_d_echeance']} - État: {task['etat']}")
        
        field = input("Quel champ souhaitez-vous mettre à jour (nom/description/date/etat) ? ").lower()

        if field in task:
            task[field] = input(f"Nouvelle valeur pour {field.capitalize()} : ")
            print("Tâche mise à jour avec succès!")
        else:
            print("Champ invalide!")
    else:
        print("Numéro de tâche invalide!")

def supprimer_tache():
    afficher_taches()
    choix = int(input("Choisissez le numéro de la tâche à supprimer : ")) - 1

    if 0 <= choix < len(tasks):
        deleted_task = tasks.pop(choix)
        print(f"Tâche supprimée avec succès : {deleted_task['nom']}")
    else:
        print("Numéro de tâche invalide!")

while True:
    print("\nFaites votre choix:")
    print("1-Afficher toutes les tâches")
    print("2-Ajouter une tâche")
    print("3-Mettre à jour une tâche")
    print("4-Supprimer une tâche")
    print("5-Quitter")

    choix_utilisateur = input("Entrez le numéro de votre choix : ")

    if choix_utilisateur == "1":
        afficher_taches()
    elif choix_utilisateur == "2":
        ajouter_tache()
    elif choix_utilisateur == "3":
        mettre_a_jour_tache()
    elif choix_utilisateur == "4":
        supprimer_tache()
    elif choix_utilisateur == "5":
        print("Merci d'avoir utilisé le gestionnaire de tâches. Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")
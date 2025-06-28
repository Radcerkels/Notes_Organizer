#utf-8
import os
from datetime import datetime
import shutil



def Organize_notes():
    Classification = {} #Dict pour ranger les notes par thème
    with open("my_notes.txt" , "r") as file:
        for line in file:
            index = line.index(":")
        
            if line[:index] not in Classification:
                Classification[line[:index]] = []
            Classification[line[:index]].append(line[index + 1:])
    print("Notes classees par type dans un dictionnaire avec succes !")
    return Classification



def Archive_notes():            
    if not os.path.exists("Archives"):
        os.mkdir("Archives")

    #Prendre la date et l'heure de my_notes.txt
    
    time = datetime.now().strftime("%Y-%m-%d")
    new_name = f"my_notes_{time}.txt"

    destination = os.path.join("Archives" , new_name)

    shutil.move("my_notes.txt",destination)

    with open("my_notes.txt" , "w") as file:
        file.write("")
    print("Notes archivees avec succes !")



def Organize_by_theme(Classification , output_dir = "Sub_notes"):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for theme , notes in Classification.items():
        # Nettoyer le nom
        theme_name = theme.strip().replace(" ", "_").replace("#", "")
        chemin_fichier = os.path.join(output_dir, f"{theme_name}.txt")

        mode = "a" if os.path.exists(chemin_fichier) else "w"
        with open(chemin_fichier, mode , encoding="utf-8") as file:
            for note in notes:
                file.write(note)

        print("Notes classees par type dans des fichiers texte avec succes !")



Organize_by_theme(Organize_notes() , "Sub_notes")

if not os.path.exists("Sub_notes"):
    os.mkdir("Sub_notes")
chemin = os.path.abspath("Sub_notes")
mother = os.path.dirname(chemin)
for element in os.listdir(mother):
    if element.endswith(".txt") and element != "my_notes.txt":
        shutil.move(os.path.join(mother, element), chemin)
print("Notes déplacées avec succès dans le dossier Sub_notes !")

Archive_notes()

#utf-8
import os
import datetime
import shutil



def Organize_notes():
    Classification = {} #Dict pour ranger les notes par thème
    with open("my_notes.txt", "r") as file:
        for line in file:
            index = line.index(":")
            if line[:index] not in Classification:
                Classification[line[:index]] = []
            Classification[line[:index]].append(line[index + 1:])
    print("Notes classees par type dans un dictionnaire avec succes !")
    return Classification


"""""
def Archive_notes():            #Incomplet
    if not os.path.exists("Archives"):
        os.mkdir("Archives")
    #Prendre la date et l'heure de my_notes.txt
    horodatage = os.path.getmtime("my_notes.txt")
    date = datetime.datetime.fromtimestamp(horodatage)
    chemin = os.path.dirname(os.path.abspath("Archives"))
    mother = os.path.dirname(chemin)

    os.rename("my_notes.txt",f"Archives/my_notes_{date}.txt")
    shutil.move(os.path.join(mother,f"Archives/my_notes_{date}.txt"),chemin)
    print("Notes archivees avec succes !")
"""""


def Organize_by_theme(Classification):
    for theme in Classification.keys():
        if not os.path.exists(f"{theme}.txt"):
            file = open(f"{theme}.txt", "w")
        else:
            file = open(f"{theme}.txt", "a")
        for note in Classification[theme]:
            file.write(note)
        file.close()
        print("Notes classees par type dans des fichiers texte avec succes !")



Organize_by_theme(Organize_notes())

if not os.path.exists("Sub_notes"):
    os.mkdir("Sub_notes")
chemin = os.path.abspath("Sub_notes")
mother = os.path.dirname(chemin)
for element in os.listdir(mother):
    if element.endswith(".txt") and element != "my_notes.txt":
        shutil.move(os.path.join(mother, element), chemin)
print("Notes déplacées avec succès dans le dossier Sub_notes !")



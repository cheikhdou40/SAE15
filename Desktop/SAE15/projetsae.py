import os
import csv



def lecture_fichier(chemin: str):
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None


heure = []
ipsr = []
ipde = []
flag = []
seq = []
longueur = []

file = open('C:/Users/Moi/Desktop/SAE15/Fichier_a_traiter.txt', "r")
   
for line in file:
    if "IP" in line:
        separation=line.split(" ")
        heure.append(separation[0])
        ipsr.append(separation[2])
        ipde.append(separation[1])
        flag.append(separation[6])
        seq.append(separation[4])
        if "HTTP" in line:
            longueur.append(separation[-2])
        else:
            longueur.append(separation[-1])
            
    
    
with open('C:/Users/Moi/Desktop/donnees.csv', "w" , newline='') as Fichier_a_traitercsv:
        writer = csv.writer(Fichier_a_traitercsv)
        writer.writerow(['heure','IP source','IP destination','Flag','seq','lenght'])
        writer.writerows(zip(heure,ipsr,ipde,flag,seq,longueur))
        Fichier_a_traitercsv.close()

file.close()


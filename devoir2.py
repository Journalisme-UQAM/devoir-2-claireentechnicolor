#coding: utf-8
#j'importe le fichier csv pour pouvoir extraire les données

import csv

import re

fichier = "concordia1.csv"

f1 = open(fichier)

lignes = csv.reader(f1)

for ligne in lignes:
    titre = ligne[2] #définissons les variables demandées
    longTitre = len(ligne[2])  #pour avoir la longueur du titre on utilise len
    type = ligne[7]
    nbPages = ligne[6]
    
    print("titre" + "longTitre" + "type" + "nbPages")
    
    
    #mon script ne fonctionne pas... je m'y attendais. J'ai essayé d'y aller le plus simplement possible mais de toute évidence,
    #je n'y comprends encore pas grand chose. Les chiffres romains? quels chiffres romains?
    

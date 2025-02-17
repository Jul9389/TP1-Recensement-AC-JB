import csv

doc8 = "donnees_2008.csv"
doc16 = "donnees_2016.csv"
with open(doc8, newline='', encoding='utf-8') as csvfile: #ne pas effectuer de retour à la ligne et encodage pour la langue
	
	lecteur = csv.DictReader(csvfile) #considérer chaque ligne comme un dico pour pouvoir trier par colonne

	for ligne in lecteur :
		 if ligne['Nom de la région'].strip().lower() == 'bourgogne' and ligne['Code département'].strip() == '89': #éviter les espaces inutiles et convertir toute la chaine en minuscule afin de trouver le mot peut importe l'écriture 
            		print(f"Commune : {ligne['Nom de la commune']}, Population totale : {ligne['Population totale']}")

with open(doc16, newline='', encoding='utf-8') as csvfile:
    lecteur16 = csv.DictReader(csvfile)
    
    for ligne in lecteur16:
        if ligne['Nom de la région'].strip().lower() == 'bourgogne' and ligne['Code département'].strip() == '89':
            print(f"Commune (2016) : {ligne['Nom de la commune']}, Population totale : {ligne['Population totale']}")

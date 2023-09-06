"""
/**
* 1
 * projet python du pdf examenSn
 *
 * Copyright (c) 2023 NGUENA ZEBS
 * Student ICT - UNIVERSITY
 * CEO NGcodeX OS CLUB
 *
 *
 * Tous droits réservés. Ce code source est sous la licence MIT.
 * Vous pouvez utiliser ce fichier, sauf conformément à la licence en vigueur.
 * Pour plus de détails, veuillez consulter le fichier LICENSE.
 *
 * GitHub: github.com/codeurzebs
 * Site web : ngcodex.com
 * Contact : Yaoundé, CAMEROUN
 * Valide BP: 7761 Yaoundé, Cameroun
 */
"""

# TOUTE LES EXEPTIONS SONT GEREES Y COMPRIS LES CARACTERES EN STRING OU NBRE NEGATIFS

import random
import time # Ici je voulais gerer meme le temps de lancement mais y avais plus de temps

mise = 0
benef = 0
netp = 0
gain = 0
gainpartie = 0
reponse = 1
misetotal = 0

def lancer_de():
    return random.randint(1, 6)  # je simule le lancer d'un dé en utilisant randint() de 1 a 6.

print("===============BIENVENUE DANS MON PROGRAMME DE DE====================\n\n")

while reponse == 1 :

    print("la mise par partie est de 10 UNITES \n")
    mise =  input("Entrer votre mise pour lancer la partie (10):")
    while (not mise.isdigit()) or (int(mise) < 0) or (int(mise) < 10 and int(mise) > 0):
        print("la mise par partie est de 10 UNITES ")
        mise = input("___CARACTERE ERROR____ svp entrez une valeur positive de votre mise pour lancer la partie (10U): ")
    mise = int(mise)

    start = input("******Entrer la touche 'L' pour lancer le dee ou  'S' pour sortir du jeu: ")

    while not (start == "L" or start == "l" or start == "s" or start == "S") :
        start = str(input(f"Ouuppss désolé 'CARACTERE__ERROR' Bien vouloir Entrer la touche 'L' pour lancer le dee ou  'S' pour sortir du jeu: "))
    start = start.upper()

    if start == "S" :
        print("\n===============FIN DU JEU====================\n")
        misetotal = mise
        reponse = 0
    else:
        print("...encours")
        result = lancer_de()
        print(f"le De a ete Lancer avec succes le chiffre apparue est : {result}")

        if result == 1 :
            gain = 3
        if result == 3 :
            gain = -2
        if result == 4 :
            gain = -3
        if result == 5 :
            gain = -5
        if result == 6 :
            gain = 7

        gainpartie = mise + gain
        misetotal += mise
        netp = misetotal + gainpartie
        benef += gain
        print(f" GainPartie = {gain} U ")
        print(f"Mise = {mise}")
        print(f"Total = {gainpartie}")

        if gainpartie > 0:
            reponse = input("******Voulez vous continuer le jeu?? si oui Entrer la lettre 'O' si non entrer la lettre 'N': ")
            while not (reponse == "N" or reponse == "n" or reponse == "o" or reponse == "O"):
                reponse = input("___CARACTERE ERROR____ svp si oui Entrer le numero 1 si non entrer le numero 0: ")
            if reponse == "0" or reponse == "o":
                reponse = 1
            else:
                reponse = 0
        if gainpartie < 0:
            print("***********SOLDE INSUFFISANT. entrer une nouvelle mise*************")
            reponse = input("******Voulez vous faire une nouvelle mise pour continuer le jeu?? si oui Entrer le numero 1 si non entrer le numero 0: ")
            while not (reponse == "N" or reponse == "n" or reponse == "o" or reponse == "O"):
                reponse = input("___CARACTERE ERROR____ svp si oui Entrer le numero 1 si non entrer le numero 0: ")
            if reponse == "0" or reponse == "o":
                reponse = 1
            else:
                reponse = 0
                mise = 0
                netp = 0
                gainpartie = 0


print("****************RESULTAT VOS PARTIE*****************")

print(f" MISE TOTALE = {misetotal}")
print(f" BENEFICE TOTAL = {benef}")
print(f" NET A PERCEVOIR = {netp}")

print("\n\n===============FIN DU PROGRAMME MERCI====================\n")
print("==================PAR: Codeur ZEBS de ICT UNIVERSITY===========================")

"""
/**
* 1
 * projet python du pdf examenSn
 *
 * Copyright (c) 2023 NGUENA ZEBS
 * Student ICT - UNIVERSITY
 * CEO NGcodeX OS CLUB
 *
 *
 * Tous droits réservés. Ce code source est sous la licence MIT.
 * Vous pouvez utiliser ce fichier, sauf conformément à la licence en vigueur.
 * Pour plus de détails, veuillez consulter le fichier LICENSE.
 *
 * GitHub: github.com/codeurzebs
 * Site web : ngcodex.com
 * Contact : Yaoundé, CAMEROUN
 * Valide BP: 7761 Yaoundé, Cameroun
 */
"""



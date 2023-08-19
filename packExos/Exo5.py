print("**********Bienvenue dans mon Programme de multiplication************")
CONST = 10
refaire = -1
"""
/**
 * projet python du pdf ExPythonMultiplication.pdf
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
while refaire != 1:
    br = 0
    mr = 0
    print("\n Vous avez une serie de 10 multiplication a faire\n \t **********Bonne Chance!!!!")
    for i in range(CONST):
        print(f"\n==========TEST NUMERO {i + 1}: ================")
        nbre1 = input(f"entrer votre 1er nbre comprise entrer 1 et {CONST}: ")
        while not nbre1.isdigit():
            nbre1 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
        nbre1 = int(nbre1)
        while (nbre1 > CONST) or (nbre1 <= 0):
            nbre1 = input(f"Ouuppss désolé entrer un le 1 er nbre compris entre 1 et {CONST}: ")
            while not nbre1.isdigit():
                nbre1 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
            nbre1 = int(nbre1)

        nbre2 = input(f"Entrer un 2 em nbre compris entre 1 et {CONST}: ")
        while not nbre2.isdigit():
            nbre2 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
        nbre2 = int(nbre2)
        while (nbre2 > CONST) or (nbre2 <= 0):
            nbre2 = input(f"Ouuppss désolé entrer un le 2 er nbre compris entre 1 et {CONST}: ")
            while not nbre2.isdigit():
                nbre2 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
            nbre2 = int(nbre2)

        print("**********************Question****************\n")
        res = input(f"Combien font {nbre1} X {nbre2} = ???? : ")
        while not res.isdigit():
            res = input(f"Ouuppss désolé 'CARACTERE__ERROR' Combien font {nbre1} X {nbre2} = ???? :  ")
        res = int(res)
        if res != (nbre1 * nbre2):
            mr += 1
        else:
            br += 1

    print("\n********************RESULTAT DE VOTRE TEST********************")

    print(f"vous avez  {br} Reponse / {CONST} et {mr}")
    print("*********************************")
    if br < (CONST / 2):
        print(f"Retournez en CE2 : {br} bonnes réponses et {mr} mauvaises sur {CONST}.")
        print(f"Votre moyenne est = {br / 10}")
    if ((CONST / 2) < br) :
        print(f"C’est moyen : continuer d'apprendre. {br} bonnes réponses et {mr} mauvaises sur {CONST}.")
        print(f"Votre moyenne est = {br / CONST}")
    if br == CONST:
        print(f"Félicitations : {br} bonnes réponses et {mr} mauvaises sur {CONST}.")
        print(f"Votre moyenne est = {br / CONST}")

    print("***********************FIN DU TEST**********************\n")
    choix = input("Voulez vous refaire un autre test?? si oui entrer 1 si non 0:  ")
    choix = int(choix)
    if (choix == 1) :
        refaire = -1
    if (choix == 0) :
        refaire = 1
print("**************MERCI FIN DU PROGRAMME*********************")

"""
/**
 * projet python du pdf ExPythonMultiplication.pdf
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
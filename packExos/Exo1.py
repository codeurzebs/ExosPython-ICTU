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
CONST = 10
nbre1 = input("entrer votre 1er nbre comprise entrer 1 et 10: ")
while not nbre1.isdigit() :
    nbre1 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
nbre1 = int(nbre1)
while (nbre1 > CONST) or (nbre1 <= 0) :
    nbre1 = input(f"Ouuppss désolé entrer un le 1 er nbre compris entre 1 et {CONST}: ")
    while not nbre1.isdigit():
        nbre1 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
    nbre1 = int(nbre1)

nbre2 = input(f"Entrer un 2 em nbre compris entre 1 et {CONST}: ")
while not nbre2.isdigit() :
    nbre2 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
nbre2 = int(nbre2)
while (nbre2 > CONST) or (nbre2 <= 0) :
    nbre2 = input(f"Ouuppss désolé entrer un le 2 er nbre compris entre 1 et {CONST}: ")
    while not nbre2.isdigit():
        nbre2 = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer un le 1 er nbre compris entre 1 et {CONST}: ")
    nbre2 = int(nbre2)

print("**********************Question****************\n")
res = input(f"Combien font {nbre1} X {nbre2} = ???? : ")
while not res.isdigit() :
    res = input(f"Ouuppss désolé 'CARACTERE__ERROR' Combien font {nbre1} X {nbre2} = ???? :  ")
res = int(res)
if res != (nbre1 * nbre2):
    print(f"Ouuppss mauvaise reponse Domage!!!")
else:
    print(f"***************Bonne reponse Bravo!!!! {nbre1} X {nbre2} = {nbre1 * nbre2}")

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
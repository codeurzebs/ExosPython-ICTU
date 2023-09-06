"""
/**
*2
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

print("===============BIENVENUE DANS MON PROGRAMME DE DIVISION ECLIDIENNE====================\n\n")
# Les valeur que l'utilisateur va entrer pour a et b
a = input("Entrez la valeur positive de a : ")
while (not a.isdigit()) or (int(a) < 0):
    a = input("___CARACTERE ERROR____ svp entrez une valeur positive de a : ")
a = int(a)
b = input("Entrez la valeur positive de b et doit être supérieure à a svp : ")
while (not b.isdigit()) or (int(b) < 0) :
    b = input("___CARACTERE ERROR____ svp entrez la valeur positive de b et doit être supérieure à a svp : ")
b = int(b)
# ICI, je verifie que a est effectivement inférieur à b
while a >=b :
    print("********la valeur de a doit être strictement inférieur à b.********")
    a = input("Entrez la valeur positive de a : ")
    while (not a.isdigit()) or (int(a) < 0) :
        a = input("___CARACTERE ERROR____ svp entrez une valeur positive de a : ")
    a = int(a)
#  ICI, je Calcul la division euclidienne de a et b
quotient = b // a  # Division entière
reste = b % a      # Opérateur modulo
# Affichage des résultats
print(f"** La division de {b} par {a} est :")
print(f"** Quotient est : {quotient}")
print(f"** Reste est : {reste}")

print("\n\n===============FIN DU PROGRAMME MERCI====================\n")
print("==================PAR: Codeur ZEBS de ICT UNIVERSITY===========================")

"""
/**
*2
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
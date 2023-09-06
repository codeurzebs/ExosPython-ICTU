"""
/**
*4
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

print("===============BIENVENUE DANS MON PROGRAMME DE FACTORIELLE====================\n\n")
# L'utilisateur saisie le nombre dont on veut calculer le factoriel
nbre = input("Entrez un nombre entier positif svp : ")
while (not nbre.isdigit()) or (int(nbre) < 0):
    nbre = input("___CARACTERE ERROR____ svp le nombre doit être positif svp : ")
nbre = int(nbre)
result = 1
# Je calcul le factoriel en utilisant une boucle for
print(f"{nbre} = ")
for i in range(1, nbre + 1):
    result *= i
# Affichage du résultat ou le factoriel du nbre
print(f"Le factoriel de {nbre} est {result}")

print("\n\n===============FIN DU PROGRAMME MERCI====================\n")
print("==================PAR: Codeur ZEBS de ICT UNIVERSITY===========================")

"""
/**
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
"""
/**
*3
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

import random

"""
en gros, j utilise la fonction simuler_lancers(nb_lancers) pour simuler les lancers de deux dés le nombre de fois spécifié.

"""
def lancer_de():
    return random.randint(1, 6)
def simuler_lancers(nb_lancers):
    resultat_lancers = [0] * 11
    for _ in range(nb_lancers):
        somme_des = lancer_de() + lancer_de()
        resultat_lancers[somme_des - 2] += 1  # -2 car les résultats sont de 2 à 12.
    return resultat_lancers

if __name__ == "__main__":
    nb_lancers = 10000
    resultat_lancers = simuler_lancers(nb_lancers)
    print("Les Résultats des lancers sont :")
    for somme_des, nombre_lancers in enumerate(resultat_lancers, start=2):
        pourcentage = (nombre_lancers / nb_lancers) * 100
        print(f"Somme {somme_des} : {pourcentage:.2f}%")

"""
/**
*3
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
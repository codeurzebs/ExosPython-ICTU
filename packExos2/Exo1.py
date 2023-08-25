"""
/**
 * projet python du pdf ExHeure.pdf
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
ampm = input("Salut Bien vouloir definir si vous etes en AM ou PM : ")
while not (ampm == "am" or ampm == "AM" or ampm == "pm" or ampm == "PM") :
    ampm = str(input(f"Ouuppss désolé 'CARACTERE__ERROR' Bien vouloir definir AM ou PM: "))

if ampm == "am" or ampm == "AM" :
    print(f"=======================VOTRE DEFAULT EST {ampm.upper()}======================")
    heure = input("entrer une heure comprise entrer 1am et 12pm: ")
    while not heure.isdigit():
        heure = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une heure comprise entrer 1am et 12pm: ")
    heure = int(heure)
    while (heure > 12) or (heure < 1):
        heure = input(f"Ouuppss désolé entrer une heure comprise entrer 1am et 12pm: ")
        while not heure.isdigit():
            heure = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une heure comprise entrer 1am et 12pm: ")
        heure = int(heure)

    heure_avenir = input(" pendant combien d'heures avenir auquel voulez vous aller?  ")
    while not heure_avenir.isdigit():
        heure_avenir = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une  heure convenable: ")
    heure_avenir = int(heure_avenir)
    while heure_avenir < 0:
        heure_avenir = input(f"Ouuppss désolé entrer une  heure convenable positive: ")
        while not heure_avenir.isdigit():
            heure_avenir = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une  heure convenable: ")
        heure_avenir = int(heure_avenir)

    heure_def = heure + heure_avenir
    while heure_def > 24:
        heure_def = heure_def - 24

    if heure_def == 0:
        engl = "12:00 AM"
    elif heure_def < 12:
        engl = f"{heure_def}:00 AM"
    elif heure_def == 12:
        engl = "12:00 PM"
    else:
        engl = f"{heure_def - 12}:00 PM"

    print(heure_def)
    print(f"\nHeure entrer: {heure}am")
    print(f"Heure avenir definis dans: {heure_avenir}h de temps")
    print(f"nouvelle heure exact pour votre projet: {engl}")

if ampm == "pm" or ampm == "PM" :
    print(f"=======================VOTRE DEFAULT EST {ampm.upper()}======================")
    heure = input("entrer une heure comprise entrer 1am et 12pm: ")
    while not heure.isdigit():
        heure = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une heure comprise entrer 1pm et 12am: ")
    heure = int(heure)
    while (heure > 12) or (heure < 1):
        heure = input(f"Ouuppss désolé entrer une heure comprise entrer 1am et 12pm: ")
        while not heure.isdigit():
            heure = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une heure comprise entrer 1pm et 12am: ")
        heure = int(heure)

    heure_avenir = input(" pendant combien d'heures avenir auquel voulez vous aller?  ")
    while not heure_avenir.isdigit():
        heure_avenir = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une  heure convenable: ")
    heure_avenir = int(heure_avenir)
    while heure_avenir < 0:
        heure_avenir = input(f"Ouuppss désolé entrer une  heure convenable positive: ")
        while not heure_avenir.isdigit():
            heure_avenir = input(f"Ouuppss désolé 'CARACTERE__ERROR' entrer une  heure convenable: ")
        heure_avenir = int(heure_avenir)

    heure_def = heure + heure_avenir
    while heure_def > 24:
        heure_def = heure_def - 24

    if heure_def == 0:
        engl = "12:00 PM"
    elif heure_def < 12:
        engl = f"{heure_def}:00 PM"
    elif heure_def == 12:
        engl = "00:00 AM"
    else:
        engl = f"{heure_def - 12}:00 AM"

    print(heure_def)
    print(f"\nHeure entrer: {heure}pm")
    print(f"Heure avenir definis dans: {heure_avenir}h de temps")
    print(f"nouvelle heure exact pour votre projet: {engl}")

"""
/**
 * projet python du pdf ExHeure.pdf
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

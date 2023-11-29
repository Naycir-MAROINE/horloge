import time

def afficher_heure(heure, mode_12_heures=False):
    if mode_12_heures:
        suffixe = "AM" if heure[0] < 12 else "PM"
        heure_format = "{:02d}:{:02d}:{:02d} {}".format((heure[0] % 12) or 12, heure[1], heure[2], suffixe)
    else:
        heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format)

def regler_heure():
    heures = int(input("Heures : "))
    minutes = int(input("Minutes : "))
    secondes = int(input("Secondes : "))
    return heures, minutes, secondes

def afficher_heure_et_regler():
    heure_actuelle = regler_heure()
    afficher_heure(heure_actuelle)

def regler_alarme():
    print("Réglage de l'alarme :")
    return regler_heure()

def choisir_mode_affichage():
    mode_12_heures = input("Choisissez le mode d'affichage (12 ou 24 heures) : ").lower() == "12"
    return mode_12_heures

def mettre_en_pause():
    input("Appuyez sur Entrée pour reprendre l'horloge...")
    
def verifier_alarme(heure_actuelle, alarme):
    if alarme and heure_actuelle == alarme:
        print("Alarme ! L'heure de l'alarme est atteinte.")

def programme_horloge():
    mode_12_heures = choisir_mode_affichage()
    heure_actuelle = (0, 0, 0)
    alarme = regler_alarme()

    while True:
        afficher_heure(heure_actuelle, mode_12_heures)
        verifier_alarme(heure_actuelle, alarme)

        try:
            time.sleep(1)
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)

            if heure_actuelle[2] == 60:
                heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)

            if heure_actuelle[1] == 60:
                heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])

            if heure_actuelle[0] == 24:
                heure_actuelle = (0, 0, heure_actuelle[2])

        except KeyboardInterrupt:
            print("\nHorloge en pause.")
            mettre_en_pause()

    print("Programme terminé.")

if __name__ == "__main__":
    print("Réglage de l'heure actuelle :")
    afficher_heure_et_regler()

    print("Programme d'horloge en cours...")
    programme_horloge()
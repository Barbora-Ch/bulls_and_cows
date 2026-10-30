import random
import time

DELKA = 4


def vygeneruj_cislo() -> str:
    """
    Vygeneruje náhodné 4-místné číslo, kde každá číslice je unikátní a první číslice není nula.
    """
    prvni_cislice = random.choice("123456789")
    dalsi_cislice = "0123456789".replace(prvni_cislice, "")
    druha_cislice = random.choice(dalsi_cislice)
    dalsi_cislice = dalsi_cislice.replace(druha_cislice, "")
    treti_cislice = random.choice(dalsi_cislice)
    dalsi_cislice = dalsi_cislice.replace(treti_cislice, "")
    ctvrta_cislice = random.choice(dalsi_cislice)

    return prvni_cislice + druha_cislice + treti_cislice + ctvrta_cislice


def over_zadane_cislo(hadani: str, delka: int) -> bool:
    """
    Ověřuje, zda zadané číslo splňuje podmínky hry.
    """
    if len(hadani) != delka:
        print("Please enter exactly " + str(delka) + " digits.")
        return False
    elif not hadani.isdigit():
        print("Please enter a number.")
        return False
    elif len(set(hadani)) != delka:
        print("Please enter a number with unique digits.")
        return False
    elif hadani[0] == "0":
        print("The first digit cannot be zero.")
        return False
    else:
        return True


def spocitej_bulls_and_cows(pc_cislo: str, hadani: str) -> tuple[int, int]:
    """
    Počítá počet "bulls" a "cows" na základě zadaného čísla a čísla vygenerovaného počítačem.
    """
    bulls = 0
    cows = 0

    for cislice in pc_cislo:
        if cislice in hadani:
            if cislice == hadani[pc_cislo.index(cislice)]:
                bulls = bulls + 1
            else:
                cows = cows + 1

    return bulls, cows


def vypis_bulls_and_cows(bulls: int, cows: int) -> str:
    """
    Tato funkce vypíše počet "bulls" a "cows".
    """
    if bulls == 1:
        slovo_bulls = "bull"
    else:
        slovo_bulls = "bulls"

    if cows == 1:
        slovo_cows = "cow"
    else:
        slovo_cows = "cows"

    return str(bulls) + " " + slovo_bulls + ", " + str(cows) + " " + slovo_cows


def preved_cas_na_minuty(trvani: int) -> str:
    """
    Převede celkový počet sekund na text s minutami a sekundami.
    """
    minuty = trvani // 60
    sekundy = trvani % 60

    if sekundy == 1:
        slovo_sekundy = "second"
    else:
        slovo_sekundy = "seconds"

    if minuty == 1:
        slovo_minuty = "minute"
    else:
        slovo_minuty = "minutes"

    if minuty == 0:
        return str(sekundy) + " " + slovo_sekundy
    else:
        return (str(minuty) + " " + slovo_minuty + " " 
         + str(sekundy) + " " + slovo_sekundy)


def spust_hru() -> None:
    """
    Tato funkce spustí hru.
    """
    pc_cislo = vygeneruj_cislo()
    # print(pc_cislo) # pouze pro test

    pokusy = 0

    print("Hi there!")
    print("-" * 47)
    print("I've generated a random " + str(DELKA) + " digit number for you.")
    print("Let's play a bulls and cows game!")
    print("-" * 47)
    print("Enter a number:")
    print("-" * 47)

    start_cas = time.time()

    while True:
        hadani = input(">>> ")
        if not over_zadane_cislo(hadani, DELKA):
            print("-" * 47)
            continue

        pokusy = pokusy + 1

        if pokusy == 1:
            slovo_pokusy = "guess"
        else:
            slovo_pokusy = "guesses"

        if hadani == pc_cislo:
            konec_cas = time.time()
            trvani = round(konec_cas - start_cas)
            formatovany_cas = preved_cas_na_minuty(trvani)
            print("Correct, you've guessed the right number\nin " 
                  + str(pokusy) + " " + slovo_pokusy + "!")
            print("It took you " + str(formatovany_cas) + ".")
            print("-" * 47)
            print("That's amazing!")
            break

        bulls, cows = spocitej_bulls_and_cows(pc_cislo, hadani)
        print(vypis_bulls_and_cows(bulls, cows))
        print("-" * 47)


if __name__ == "__main__":
    spust_hru()

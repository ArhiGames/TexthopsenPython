import string

proccessing_text = ""
bela_index = 0
amira_index = 1

# hier wollen wir testen, ob das Feld auf das wir versuchen zu springen überhaupt ein uns
# bekanntes ist (valides Feld); wir nehmen als ersten Parameter also den Index zu dem char
# aus der Liste des gesammten Textes (auch ein String ist tiefer gesehen eine Liste!)
def is_valid_field(index: int) -> bool:
    # nur wenn der Index im Bereich der Liste ist, machen wir weiter
    if 0 <= index < len(proccessing_text):
        processing_char = proccessing_text[index]
        # isalpha beinhaltet alle Buchstaben von a - z; nicht aber ä, ö, ü, ö
        # deswegen prüfen wir diese nochmal seperat
        return processing_char.isalpha() or processing_char in 'äöüß'
    return False

# erster parameter: den charakter, von dem die Sprunglänge ermittelt werden soll
# rückgabe: die korrekte sprungweite
def get_jump_length(character: str) -> int:
    # hier nutzen wir den ASCII Code, jeder Buchstabe hat eine eindeutliche Zahl
    # die diesem zugeordnet ist, ein kleine "a" hat z.B. den Code 97; Ein großes "A"
    # hat den Code 65, ein "B" die 66 usw...
    # daher machen wir mit der .lower funktion jeden Buchstaben zu einem klein Buchstaben
    # dann können wir weiter machen
    letter = character.lower()

    # diese buchstaben passen nicht mit dem Rest unserer "Formel" zusammen, daher
    # geben wir hier direkt die richtige Sprungweite zurück
    if letter == 'ä':
        return 27
    elif letter == 'ö':
        return 28
    elif letter == 'ü':
        return 29
    elif letter == 'ß':
        return 30

    # da jeder Buchstabe jetzt ein klein Buchstabe ist, können wir diesen - 96 rechnen
    # z.B.: kleines a (97): 97 - 96 = 1; Bei einem kleinen a springen wir also 1 Feld;
    # z.B.: kleines c (99): 99 - 96 = 3; bei einem kleinen c springen wir also 3 Felder;
    return ord(letter) - 96


def jump_to(index: int) -> int:
    new_index = index
    while new_index < len(proccessing_text) and not is_valid_field(new_index):
        new_index += 1

    return new_index


def get_text_to_proccess(arg: str) -> str:
    if len(arg) >= 4 and arg.endswith(".txt"):
        try:
            with open(arg, 'r', encoding='utf-8') as file:
                print(f"[Success] Could successfully open a file with name {arg} :)")
                return file.read()
        except FileNotFoundError:
            print(f"[Error] Could not open file with name {arg} :(")
            return arg

    return arg


def main() -> None:
    global proccessing_text, bela_index, amira_index

    while True:
        proccessing_text = input("Bitte gebe den zu spielenden Text ein: \n")
        proccessing_text = get_text_to_proccess(proccessing_text)

        i = 0
        while True:
            if i % 2 == 0:  # Bella ist dran
                bela_index += get_jump_length(proccessing_text[bela_index])
                if bela_index >= len(proccessing_text):
                    print("Bella hat gewonnen!")
                    break
                bela_index = jump_to(bela_index)
            else:  # Amira ist dran
                amira_index += get_jump_length(proccessing_text[amira_index])
                if amira_index >= len(proccessing_text):
                    print("Amira hat gewonnen!")
                    break
                amira_index = jump_to(amira_index)

            i += 1

        another_round = input("Willst du nochmal spielen? Yes[Y], No[N]: ").strip()
        if another_round.upper() != "Y":
            break

        bela_index = 0
        amira_index = 1
        proccessing_text = ""


if __name__ == "__main__":
    main() #diese methode wird aufgerufen, wenn das Programm startet

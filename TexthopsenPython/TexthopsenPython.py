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

# funktion um direkt zu einem bestimmten Feld zu springen
def jump_to(index: int) -> int:
    new_index = index
    # hier korriegeren wir den Ort wo hingesprungen werden soll, wenn wir versuchen
    # auf ein nicht valides Feld zu springen, korriegieren wir die Position bis
    # wir ein valides Feld haben
    while new_index < len(proccessing_text) and not is_valid_field(new_index):
        new_index += 1

    return new_index

# wenn man einen pfad zu einer .txt Datei eingibt, versucht er diese Datei zu öffnen
# wenn er das schafft, gibt er den Content der Datei als String zurück. Sonst gibt er
# den eingegebenen Text zurück
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
        # Hier bitten wir den Nutzer, den Pfad zu einer .txt Datei einzugeben
        # oder auch direkt ohne die Endung .txt
        proccessing_text = input("Bitte gebe den zu spielenden Text ein: \n")
        proccessing_text = get_text_to_proccess(proccessing_text)
        # get_text_to_proccess gibt uns wie oben gesagt, den gelesenen Text zurück

        # Dieser Abschnitt sollte relativ selbst erklärend sein
        # while True geht die Schleife solange durch, bis sie manuell abgebrochen wurde
        i = 0
        while True:
            # Zuerst springen wir für Bella, dann für Amira...
            if i % 2 == 0:  # Bella ist dran
                bela_index += get_jump_length(proccessing_text[bela_index])
                # bela_index steht dafür, an welcher Stelle des Textes sich Bela
                # aktuell befindet, wir holen uns für diese Stelle die richtige Sprunglänge
                # und springen zur neuen Stelle.
                if bela_index >= len(proccessing_text):
                    # Wenn wir am Ende des Textes sind, brechen wir die while Schleife ab
                    # und geben aus, das Bella gewonnen hat
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

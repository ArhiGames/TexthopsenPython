# alle Buchstaben die eine festgegebene sprungweite haben sind in dieser liste, alle anderen werden vollständig
# ignoriert
VALID_CHARACTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", "ä", "ö", "ü", "ß"]
#initiale globale variablen
processing_text: str = ""


# wenn man einen pfad zu einer .txt Datei eingibt, versucht er diese Datei zu öffnen
# wenn er das schafft, gibt er den Content der Datei als String zurück. Sonst gibt er
# den eingegebenen Text zurück
def get_text_to_proccess(arg: str) -> str:
    if len(arg) >= 4 and arg.endswith(".txt"):
        try:
            with open(arg, 'r', encoding='utf-8') as file:
                print(f"[Success] Could successfully open a file with name {arg} :)")
                return file.read().strip().lower()  # wir machen großbuchstaben DIREKT zu Kleinbuchstaben
            # Klein und Großbuchstaben machen keinen Unterschied und führen zur gleichen Sprungweite
        except FileNotFoundError:
            print(f"[Error] Could not open file with name {arg} :(")
            return arg

    return arg


# diese funktion gibt uns die sprungweite als int zurück (Ganzzahl)
def get_jump_length(arg: int) -> int:
    global processing_text
    # die .index Methode gibt uns zurück an welcher Stelle der Liste sich das Argument befindet, da Listen mit
    # 0 anfangen, rechnen wir am Ende noch + 1
    # abc = ["a", "c", "d"]
    # print(abc.index("a")) gibt uns z.B. 0 zurück, "a" ist an der ersten Stelle der Liste
    # print(abc.index("d")) gibt uns z.B. 2 zurück, "d" ist an der dritten Stelle der Liste
    jump_length: int = VALID_CHARACTERS.index(processing_text[arg]) + 1
    return jump_length


# wir löschen in dieser funktion alle buchstaben aus dem text, die wir sowieso ignorieren würden
# dazu machen wir eine neue liste, und fügen nur Buchstaben hinzu, die sich auch in der VALID_CHARACTERS
# Liste befinden
def format_text_correctly(text: str) -> str:
    global VALID_CHARACTERS
    return_value: str = ""
    for character in text:
        if character in VALID_CHARACTERS:  # wenn character in der Liste ist
            return_value += character
    return return_value


def main() -> None:
    global processing_text

    while True:
        # Hier sind unsere Werte für die Runde
        bela_index: int = 0  # bela_index ist wo sich bela aktuell im Text befindet, 0 ist bei einer Liste immer 
        # das erste Element!
        amira_index: int = 1  # amira_index ist wo sich amira aktuell im Text befindet
        processing_text = ""  # der text den wir durchgehen, ist aktuell leer

        user_input: str = input("Bitte gebe einen Pfad zu einer .txt Datei an! ")  # hier bitten wir den Benutzer
        # in der Eingabeaufforderung den Pfad zu einer .txt Datei einzugeben
        text: str = get_text_to_proccess(user_input)  # wir holen uns was in der datei drin stand, aber alle
        # Großbuchstaben sind bereits Kleinbuchstaben
        processing_text = format_text_correctly(text)  # hier entfernen wir alle Buchstaben, die nicht in unserer
        # VALID_CHARACTERS Liste sind

        bela_jump_count: int = 0  # wie viele Sprünge hat Bela gebraucht?
        amira_jump_count: int = 0  # wie viele Sprünge hat Amira gebraucht?
        while True:
            jump_length: int = get_jump_length(bela_index)  # wir holen uns die sprungweite vom zugehörigen Buchstaben
            # bei dem sich bela aktuell befindet
            bela_jump_count += 1  # bela ist eins gesprungen
            if len(processing_text) - 1 < bela_index + jump_length:
                break  # wenn wir uns mit dem nächsten Sprung aus dem Text rausbegeben würden, brechen wir die while 
                # Schleife ab, Bela ist fertig
            else:
                bela_index += jump_length  # bela befindet sich jetzt jump_length weiter

        while True:
            # wir machen hier das gleiche wie bei bela, nur halt mit amira...
            jump_length: int = get_jump_length(amira_index)
            amira_jump_count += 1
            if len(processing_text) - 1 < amira_index + jump_length:
                break
            else:
                amira_index += jump_length

        # Hier geben wir den Gewinner aus, der, der weniger Sprünge gebraucht hat, ist natürlich der Gewinner, in dieser
        # Implemenation gibt es außerdem auch Unentschieden
        # PS: Ich weiß gerade nicht mehr, ob das in der Aufgabe Pflicht war, aber hier ist es einfach mal ;)
        if bela_jump_count < amira_jump_count:
            print("Bela hat gewonnen mit {0} Sprüngen gewonnen! Amira hat nur {1}".format(str(bela_jump_count),
                                                                                          str(amira_jump_count)))
            # print("Bela hat gewonnen mit " + str(bela_jump_count) + " Sprüngen gewonnen! Amira hat nur " + str(amira_jump_count))
            # Beide Varianten sind möglich, die erste ist aber professioneller ;)
        elif amira_jump_count < bela_jump_count:
            print("Amira hat gewonnen mit {0} Sprüngen gewonnen! Bela hat nur {1}".format(str(amira_jump_count),
                                                                                          str(bela_jump_count)))
            # print("Amira hat gewonnen mit " + str(amira_jump_count) + " Sprüngen gewonnen! Bela hat nur " + str(bela_jump_count))
            # Beide Varianten sind möglich, die erste ist aber professioneller ;)
        elif bela_jump_count == amira_jump_count:
            print("Unentschieden, beide haben " + str(bela_jump_count) + " Sprünge!")


if __name__ == "__main__":
    main()

import string

proccessing_text = ""
bela_index = 0
amira_index = 1


def is_valid_field(index: int) -> bool:
    if 0 <= index < len(proccessing_text):
        processing_char = proccessing_text[index]
        return processing_char.isalpha() or processing_char in 'äöüß'
    return False


def get_jump_length(character: str) -> int:
    letter = character.lower()

    if letter == 'ä':
        return 27
    elif letter == 'ö':
        return 28
    elif letter == 'ü':
        return 29
    elif letter == 'ß':
        return 30

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


def main():
    global proccessing_text, bela_index, amira_index

    while True:
        proccessing_text = input("Bitte gebe den zu spielenden Text ein: \n")
        proccessing_text = get_text_to_proccess(proccessing_text)

        i = 0
        while True:
            if i % 2 == 0:  # Bella's turn
                bela_index += get_jump_length(proccessing_text[bela_index])
                if bela_index >= len(proccessing_text):
                    print("Bella hat gewonnen!")
                    break
                bela_index = jump_to(bela_index)
            else:  # Amira's turn
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
    main()

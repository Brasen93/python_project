import enigma
welcome_message = "Witaj w maszynie szyfrującej i deszyfrującej!"
choosing_options = "Wybierz jedną z opcji: \n" \
                   "1 - Szyfrowanie \n" \
                   "2 - Deszyfrowanie \n" \
                   "3 - Wyjscie \n"
print(welcome_message)
user_input = ''

cypher = enigma.Enigma(['a', 'e', 'i', 'o', 'y'], ['y', 'i', 'o', 'a', 'e'])
decypher = enigma.Enigma(['y', 'i', 'o', 'a', 'e'], ['a', 'e', 'i', 'o', 'y'])

while user_input.lower() not in ["wyjscie", "wyjście", "3"]:
    user_input = input(choosing_options)

    if user_input.lower() in ["szyfrowanie", "1"]:
        user_sentence = input("Podaj zdanie do szyfrowania: \n")
        print("Oto twoje zaszyfrowane zdanie: " + cypher.enigmator(user_sentence))
    elif user_input.lower() in ["deszyfrowanie", "2"]:
        user_sentence = input("Podaj zdanie do deszyfrowania: \n")
        print("Oto twoje odszyfrowane zdanie: " + decypher.enigmator(user_sentence))
    elif user_input.lower() in ["wyjscie", "wyjście", "3"]:
        print("Dziękuję za użycie maszyny szyfrującej.\nDo zobaczenia następnym razem!")
    else:
        print("Bledna operacja!")







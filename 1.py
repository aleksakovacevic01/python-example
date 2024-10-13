text = """ Chose one optios:
1) Create
2) Read
3) Quit
4) Delete
5) Update
"""

mapa = {}
while True:
    print(text)
    option = input("Input: ")
    if option == '1':
        k = input("Word: ")
        v = input("Meaning: ")
        if k not in mapa:
            mapa[k] = [v]

        else:
            mapa[k].append(v)

    elif option == '2':
        print(mapa)
    elif option == '3':
        print('quit')
        quit()
    elif option == '4':
        print("Type the word you want to delete")
        rec = input("Input: ")
        if rec in mapa:
            del mapa[rec]
            print("Successfully"+ rec)
        elif rec in mapa:
            del mapa[rec]
    elif option == '5':
        print("Current words and meanings:")
        for i, (word, meanings) in enumerate(mapa.items()):
            print(f"{i}: {word} - {meanings}")
            
        try:
            index = int(input("Enter the index of the word you want to update: "))
            if index < 0 or index >= len(mapa):
                print("Invalid index.")
                continue
            
            word_to_update = list(mapa.keys())[index]
            new_word = input("Enter the new word (or press enter to keep it the same): ")
            new_meaning = input("Enter the new meaning: ")

            # Update the word if a new word was provided
            if new_word:
                print(mapa)
                mapa[new_word] = [new_meaning]  # Zamenjujemo značenje
                print(mapa)
                if word_to_update != new_word:  # Ako se reč promenila, obrišemo staru
                    del mapa[word_to_update]
            else:
                # Samo ažuriramo značenje
                mapa[word_to_update] = [new_meaning]

            print(f"Updated '{word_to_update}' to '{new_word}' with meaning '{new_meaning}'.")
        except ValueError:
            print("Please enter a valid number.")





        
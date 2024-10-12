text = """ Chose one optios:
1) Create
2) Read
3) Quit
4) Delete
5) Update
"""

mapa = {}
while True:
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
        rec = input("Input: ")
        if rec in mapa:
            del mapa[rec]
            print("Successfully"+ rec)
        elif rec in mapa:
            del mapa[rec]
    elif option == '5':
        rec = input("Input: ")
        if rec not in mapa:
            print("ERROR")
            continue
        c = mapa[rec]
    
    # Prikaz svih reči sa njihovim indeksima
        print("Trenutne reči u mapi:")
        for i, word in enumerate(c):
            print(f"{i}: {word}")

    # Unos indeksa reči koju želiš da ažuriraš
        try:
            index = int(input("Unesite indeks reči koju želite da ažurirate: "))
            if index < 0 or index >= len(c):
                print("Nevalidan indeks.")
                continue
        except ValueError:
            print("Molimo unesite validan broj.")
            continue

    # Unos nove reči i nove vrednosti
        new_word = input("Unesite novu reč: ")
        new_value = input("Unesite novu vrednost: ")

    # Ažuriranje reči i njene vrednosti
        c[index] = new_word  # Ažuriranje reči
        c = new_value 
        mapa[rec] = c  # Ažuriramo mapu sa novom listom

        print(f"Reč na indeksu {index} je ažurirana na '{new_word}' sa vrednošću '{new_value}'.")




        
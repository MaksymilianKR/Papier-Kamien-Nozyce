Wybor_gracza1 = input('Gracz1 podaj swoj wybor: ')
Wybor_gracza2 = input('Gracz2 podaj swoj wybor: ')


if Wybor_gracza1 == 'papier':
    if Wybor_gracza2 == 'kamien':
        print("Wygrał gracz numer 1")
    elif Wybor_gracza2 == 'nozyce':
        print("Wygrał gracz 2")
    elif Wybor_gracza2 == 'papier':
        print("REMIS!")


if Wybor_gracza1 == 'kamien':
    if Wybor_gracza2 == 'kamien':
        print("REMIS!")
    elif Wybor_gracza2 == 'nozyce':
        print("Wygrał gracz 1")
    elif Wybor_gracza2 == 'papier':
        print("Wygrał gracz 2")


if Wybor_gracza1 == 'nozyce':
    if Wybor_gracza2 == 'kamien':
        print("Wygrał gracz numer 2")
    elif Wybor_gracza2 == 'nozyce':
        print("REMIS!")
    elif Wybor_gracza2 == 'papier':
        print("Wygrał gracz 1")
        

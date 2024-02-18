import getpass
from time import sleep

ilosc_gier= 0
gracz1_wynik = 0
gracz2_wynik = 0

uwaga = 'UWAGA ZARAZ WYNIK!'

poprawne_opcje = ['papier', 'kamien', 'nozyce']

while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracza_jest_poprawny = True
    while wybor_gracza_jest_poprawny:
       wybor_gracza_1 = getpass.getpass('Gracz1 podaj swoj wybor: ')
       if wybor_gracza_1 in poprawne_opcje:
          wybor_gracza_jest_poprawny = False
    
    wybor_gracza_jest_poprawny = True
    while wybor_gracza_jest_poprawny:
       wybor_gracza_2 = getpass.getpass('Gracz2 podaj swoj wybor: ')
       if wybor_gracza_2 in poprawne_opcje:
          wybor_gracza_jest_poprawny = False



    if wybor_gracza_1 == 'papier'and wybor_gracza_2 == 'kamien'\
    or wybor_gracza_1 == 'kamien'and wybor_gracza_2 == 'nozyce'\
    or wybor_gracza_1 == 'nozyce' and wybor_gracza_2 =='papier':
        print("gracz 1 wygrał!")
        gracz1_wynik += 1
    elif wybor_gracza_1 == wybor_gracza_2:
        print('Remis :)')
    else:
     print("gracz 2 wygrywa tym razem!")
     gracz2_wynik += 1
     ilosc_gier += 1

if gracz1_wynik > gracz2_wynik:
   print(uwaga)
   sleep(2)
   print("Gracz 1 WYGRYWA całą gre!")
else:
   print(uwaga)
   sleep(2)
   print("Gracz 2 WYGRYWA TERAZ CAŁĄ gre.")
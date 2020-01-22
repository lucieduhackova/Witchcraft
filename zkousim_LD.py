import csv

# oteviram a nacitam vydaje:
# 'w+' je 'w'(write) a 'r'(read) dohromady
# 'w' a 'w+' vytvori soubor, pokud jeste neexistuje
with open('testuju.csv', 'w+') as file:
    reader = csv.reader(file)
    vydaje = list(reader)

# --- "graficke" prvky -----------------------------
delici_cara = ' '+'-'*55
prazdny_radek = ' |' + ' '*53 + '|'
zacatek_radku = ' |' + ' '*2

zacatek_tabulky = f'{delici_cara}\n{prazdny_radek}'
konec_tabulky = f'{prazdny_radek}\n{delici_cara}'

# jeste muzu dodelat automaticke dopocitavani konce radku
pocet_na_radku = 56
pocet_na_zacatku_radku = 4
rozdil_znaku = pocet_na_radku - pocet_na_zacatku_radku
# konec_radku = ' '*(rozdil_znaku - len(TEXT UPROSTRED)) + '|'

# --- konec "grafickych" prvku ---------------------


# --- definovani funkci ----------------------------

# tohle by slo urcite jeste zjednodusit, ale je to jen docasne, takze se s tim neserme
# je to jen na lepsi orientaci v prikazovem konec_radku
# nakonec bychom meli mit hezkou grafiku od Peti
def show_menu():
    print()
    print(zacatek_tabulky)
    print(zacatek_radku + 'VYDAJE' + ' '*20 + 'PRIJMY' + ' '*19 + '|')
    print(prazdny_radek)
    print(zacatek_radku + '* novy vydaj (1a)' + ' '*9 + '* novy prijem (2a)' + ' '*7 + '|')
    print(zacatek_radku + '* prehled vydaju (1b)' + ' '*5 + '* prehled prijmu (2b)' + ' '*4 + '|')
    print(zacatek_radku + '* export v. do xls (1c)' + ' '*3 + '* export p. do xls (2c)' + ' '*2 + '|')
    print(prazdny_radek)
    print(prazdny_radek)
    print(zacatek_radku + '* export vydaju i prijmu do xls (3)' + ' '*16 + '|')
    print(prazdny_radek)
    print(zacatek_radku + '* ukonceni programu (4)' + ' '*28 + '|')
    print(konec_tabulky)

def question_menu():
    print(prazdny_radek)
    answer = input(' |  Jakou akci chces provest? (zadej kod): ')
    print(konec_tabulky)
    answers = ['1a', '1b', '1c', '2a', '2b', '2c', '3', '4']
    if answer == '1a':
        novy_vydaj()
        show_menu()
        question_menu()
    elif answer == '4':
        exit()
    elif answer in answers:
        print(zacatek_tabulky)
        print(zacatek_radku + 'Promin, zatim nerozumim. Jeste se ucim.' + ' '*12 + '|')
        print(konec_tabulky)
        show_menu()
        question_menu()
    else:
        print(zacatek_tabulky)
        print(zacatek_radku + 'Nerozumim.' + ' '*41 + '|')
        print(konec_tabulky)
        show_menu()
        question_menu()

def novy_vydaj():
    print(prazdny_radek)
    datum = str(input(' |  Datum (yyyy-mm-dd): '))
    kategorie = input(' |  Kategorie: ')
    cena = input(' |  Cena: ')
    poznamka = input(' |  Poznamka (volitelne): ')
    novy = [datum, kategorie, cena, poznamka]
    # return novy
    print(prazdny_radek)
    ulozit = input(' |  Ulozit? (ano/ne): ')
    print(prazdny_radek)
    if ulozit.lower() == 'ano':
        vydaje.append(novy)
        with open('testuju.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(vydaje)
        print(zacatek_radku + 'Novy vydaj ulozen.' + ' '*33 + '|')
    elif ulozit.lower() == 'ne':
        print(zacatek_radku + 'Vydaj neulozen.' + ' '*36 + '|')
    else:
        print(zacatek_radku + 'Nerozumim. Vydaj neulozen.' + ' '*25 + '|')
    print(konec_tabulky)


# holky, ja uz nevim, k cemu tohle mam, radsi to jeste necham:

# def ulozit_novy_vydaj():
#     novy = novy_vydaj()
#     print(prazdny_radek)
#     ulozit = input(' |  Ulozit? (ano/ne): ')
#     print(prazdny_radek)
#     if ulozit.lower() == 'ano':
#         vydaje.append(novy)
#         with open('testuju.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(vydaje)
#         print(zacatek_radku + 'Novy vydaj ulozen.' + ' '*33 + '|')
#     elif ulozit.lower() == 'ne':
#         print(zacatek_radku + 'Vydaj neulozen.' + ' '*36 + '|')
#     else:
#         print(zacatek_radku + 'Nerozumim. Odpovez ano/ne.' + ' '*25 + '|')
#         ulozit_novy_vydaj() # uuuuu, pouzila jsem rekurzi :D
#     print(konec_tabulky)

# --- konec definovani funkci ----------------------

# *** PRIDAT ***
# cteni zaznamu - vyber podle data nebo podle kategorie nebo obojiho


show_menu()
question_menu()

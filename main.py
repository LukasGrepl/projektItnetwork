from pojisteny import Pojisteny

print("--------------------")
print("EVIDENCE POJIŠTĚNÝCH")
print("--------------------")
pojistenci = []
volba = 1
while (volba >=1 and volba <=3):

    print("Vyberte volbu:")
    print("1 - Přidat nového pojištěného \n2 - Vypsat všechny pojištěné \n3 - Vyhledat pojištěného \n4 - Konec programu \n")
    volba = int(input("Vaše volba: "))

    if volba == 1:
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení pojištěného:\n")
        vek = input("Zadejte věk pojištěného:\n")
        telefon = input("Zadejte telefonní číslo pojištěného:\n")

        pojistenec = Pojisteny(jmeno, prijmeni, vek, telefon)
        pojistenci.append(pojistenec)

        print("Data byla uložena, pokračujte libovolnou klávesou")

    elif volba == 2:
        for name in pojistenci:
            print(name)

    elif volba == 3:
        first_name = input("Zadejte jméno: ")
        second_name = input("Zadejte příjmení: ")
        for pojistenec in pojistenci:
            if first_name == pojistenec.jmeno and second_name == pojistenec.prijmeni:
                print(pojistenec)

    elif volba == 4:
        print("Konec programu, děkuji za použití evidence pojištěných")
    else:
        print("chybná volba")


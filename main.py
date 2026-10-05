def rechner():
    print()
    print("=== Taschenrechner ===")

    while True:
        try:
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
        except ValueError:
            print("Bitte gib gültige Zahlen ein.")
            continue

        print()
        print("1 - Addieren")
        print("2 - Subtrahieren")
        print("3 - Multiplizieren")
        print("4 - Dividieren")
        print("5 - Beenden")

        auswahl = input("Auswahl: ")

        if auswahl == "1":
            ergebnis = zahl1 + zahl2
        elif auswahl == "2":
            ergebnis = zahl1 - zahl2
        elif auswahl == "3":
            ergebnis = zahl1 * zahl2
        elif auswahl == "4":
            if zahl2 == 0:
                print("Durch 0 kann man nicht teilen.")
                continue
            ergebnis = zahl1 / zahl2
        elif auswahl == "5":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl.")
            continue

        print(f"Ergebnis: {ergebnis}")


rechner()

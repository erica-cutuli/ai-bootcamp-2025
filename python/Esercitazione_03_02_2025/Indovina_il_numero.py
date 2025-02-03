import random

numero_da_indovinare = random.randint(1, 100)
tentativi = 0
trovato = False

print("Indovina un numero tra 1 e 100. Indovina!")

while not trovato:
    try:
        tentativo = int(input("Inserisci un numero:"))
    except ValueError:
        print("Input errato. Riprova.")
        continue

    tentativi += 1
    if tentativo < 1 or tentativo > 100:
        print("Fuori range! Ho detto un numero tra 1 e 100!")
    elif tentativo < numero_da_indovinare:
        print("Troppo basso! Riprova.")
    elif tentativo > numero_da_indovinare:
        print("Troppo alto! Riprova.")
    else:
        print(f"Hai indovinato in {tentativi} tentativi!")
        trovato = True
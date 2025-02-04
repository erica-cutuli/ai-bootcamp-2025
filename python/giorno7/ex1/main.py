import random
import csv
import os
from datetime import datetime

FILE_SCORE = "highscores.csv"

def ordina_per_tentativi(record):
    """Restituisce il numero di tentativi per ordinare i record"""
    return record["tentativi"]

def carica_highscore():
    """Carica i punteggi dal file CSV e restituisce una lista ordinata per tentativi"""
    records = []
    if os.path.exists(FILE_SCORE):
        with open(FILE_SCORE, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Salta l'intestazione se esiste
            for row in reader:
                try:
                    records.append({
                        "nome": row[0],
                        "tentativi": int(row[1]),  # Convertire in intero
                        "data": row[2]
                    })
                except IndexError:
                    continue  # Salta righe malformattate

    return sorted(records, key=ordina_per_tentativi)

def mostra_highscore():
    """Mostra i migliori punteggi salvati in CSV"""
    records = carica_highscore()
    if records:
        print("\n🏆 CLASSIFICA RECORD:")
        for i, rec in enumerate(records, start=1):
            print(f"{i}. {rec['nome']} - {rec['tentativi']} tentativi - {rec['data']}")
    else:
        print("\n❌ Nessun record registrato finora.")

def salva_highscore(nome, tentativi):
    """Salva un nuovo record nel file CSV con data e ora, mantenendo l'ordine"""
    data_corrente = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    records = carica_highscore()

    # Aggiungiamo il nuovo record
    records.append({"nome": nome, "tentativi": tentativi, "data": data_corrente})

    # Riordiniamo la lista per numero di tentativi
    records = sorted(records, key=ordina_per_tentativi)

    # Sovrascriviamo il file CSV con i dati ordinati
    with open(FILE_SCORE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Tentativi", "Data"])  # Intestazione
        for rec in records:
            writer.writerow([rec["nome"], rec["tentativi"], rec["data"]])

def controlla_highscore(tentativi):
    """Verifica se il giocatore ha battuto il record e aggiorna il CSV"""
    records = carica_highscore()

    # Controlla se non ci sono record o se il giocatore ha battuto il record attuale
    if not records or tentativi < records[0]["tentativi"]:
        nome = input("🎉 Hai stabilito un nuovo record! Inserisci il tuo nome: ")
        salva_highscore(nome, tentativi)
        print(f"🏆 Nuovo record registrato: {nome} con {tentativi} tentativi!")
    else:
        print(f"Non hai battuto il record attuale di {records[0]['tentativi']} tentativi.")

def gioco():
    """Gestisce una partita"""
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0
    trovato = False

    print("\n🎮 Inizia il gioco! Indovina un numero tra 1 e 100!")

    while not trovato:
        try:
            tentativo = int(input("Inserisci un numero: "))
        except ValueError:
            print("❌ Input errato. Devi inserire un numero.")
            continue

        tentativi += 1
        if tentativo < 1 or tentativo > 100:
            print("⚠️ Fuori range! Ho detto un numero tra 1 e 100!")
        elif tentativo < numero_da_indovinare:
            print("Troppo basso! Riprova.")
        elif tentativo > numero_da_indovinare:
            print("Troppo alto! Riprova.")
        else:
            print(f"🎉 Hai indovinato in {tentativi} tentativi!")
            return tentativi  # Restituisce il numero di tentativi

def main():
    """Loop principale del gioco"""
    mostra_highscore()

    while True:
        tentativi = gioco()
        controlla_highscore(tentativi)

        scelta = input("Vuoi giocare ancora? (s/n): ").strip().lower()
        if scelta != 's':
            print("\n Grazie per aver giocato! Ecco la classifica finale:")
            mostra_highscore()
            break

if __name__ == "__main__":
    main()

import sqlite3
import csv

#Carico il csv
with open("students.csv", encoding='utf-8') as fd:
    reader = csv.reader(fd, delimiter=';')
    saved_data = []
    for line in reader:
        print(line)
        saved_data.append(line)

data = saved_data[1:]

#Creo il db e carico i dati salvati dal csv
conn = sqlite3.connect("my.db")
cur = conn.cursor()

cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_of_birth INTEGER,
        gender TEXT,
        email TEXT,
        assignments INTEGER DEFAULT 0
    )''')
conn.commit()


cur.executemany(
    "INSERT INTO students "
    "(id, first_name, last_name, year_of_birth, gender, email, assignments) "
    "VALUES (?, ?, ?, ?, ?, ?, ?)"
    "ON CONFLICT DO NOTHING", #così se c'è già la riga non la aggiunge
    data
)
conn.commit()


# gli studenti nati nell'anno 2000
cur.execute("SELECT first_name, last_name "
            "FROM students "
            "WHERE year_of_birth=2000"
            )
rows = cur.fetchall()
for row in rows:
    print(row)


# la persona che ha consegnato il maggior numero di assignments
cur.execute("SELECT first_name, last_name, MAX(assignments) "
            "FROM students "
            )
rows = cur.fetchall()
for row in rows:
    print(row)


# il cognome delle studentesse di nome "Jane"
cur.execute("SELECT last_name "
            "FROM students "
            "WHERE first_name='Jane'"
            )
rows = cur.fetchall()
for row in rows:
    print(row)


# la graduatoria degli studenti ordinati in base al numero di assignment
cur.execute("SELECT first_name, last_name, assignments "
            "FROM students "
            "ORDER BY assignments DESC"
            )
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('baza.db')
    cur = conn.cursor()

    # Tworzenie tabeli uczelnia
    cur.execute('''CREATE TABLE IF NOT EXISTS uczelnia (
                    id_uczelni INTEGER PRIMARY KEY,
                    nazwa_uczelni TEXT NOT NULL
                )''')

    # Tworzenie tabeli wydział
    cur.execute('''CREATE TABLE IF NOT EXISTS wydział (
                    id_wydziału INTEGER PRIMARY KEY,
                    id_uczelni INTEGER NOT NULL,
                    nazwa_wydziału TEXT NOT NULL,
                    FOREIGN KEY (id_uczelni) REFERENCES uczelnia(id_uczelni)
                )''')

    # Tworzenie tabeli grupa_studencka
    cur.execute('''CREATE TABLE IF NOT EXISTS grupa_studencka (
                    id_grupy INTEGER PRIMARY KEY,
                    id_wydziału INTEGER NOT NULL,
                    nazwa_grupy TEXT NOT NULL,
                    FOREIGN KEY (id_wydziału) REFERENCES wydział(id_wydziału)
                )''')

    # Tworzenie tabeli wykładowca
    cur.execute('''CREATE TABLE IF NOT EXISTS wykładowca (
                    id_wykładowcy INTEGER PRIMARY KEY,
                    id_wydziału INTEGER NOT NULL,
                    imię_wykładowcy TEXT NOT NULL,
                    nazwisko_wykładowcy TEXT NOT NULL,
                    FOREIGN KEY (id_wydziału) REFERENCES wydział(id_wydziału)
                )''')

    # Tworzenie tabeli przedmiot
    cur.execute('''CREATE TABLE IF NOT EXISTS przedmiot (
                    id_przedmiotu INTEGER PRIMARY KEY,
                    id_wydziału INTEGER NOT NULL,
                    nazwa_przedmiotu TEXT NOT NULL,
                    id_wykładowcy INTEGER,
                    FOREIGN KEY (id_wydziału) REFERENCES wydział(id_wydziału),
                    FOREIGN KEY (id_wykładowcy) REFERENCES wykładowca(id_wykładowcy)
                )''')

    # Tworzenie tabeli student
    cur.execute('''CREATE TABLE IF NOT EXISTS student (
                    id_studenta INTEGER PRIMARY KEY,
                    id_grupy INTEGER NOT NULL,
                    imię_studenta TEXT NOT NULL,
                    nazwisko_studenta TEXT NOT NULL,
                    FOREIGN KEY (id_grupy) REFERENCES grupa_studencka(id_grupy)
                )''')

    # Tworzenie tabeli ocena
    cur.execute('''CREATE TABLE IF NOT EXISTS ocena (
                    id_oceny INTEGER PRIMARY KEY,
                    id_studenta INTEGER NOT NULL,
                    id_przedmiotu INTEGER NOT NULL,
                    ocena INTEGER NOT NULL,
                    FOREIGN KEY (id_studenta) REFERENCES student(id_studenta),
                    FOREIGN KEY (id_przedmiotu) REFERENCES przedmiot(id_przedmiotu)
                )''')

    conn.commit()
    conn.close()
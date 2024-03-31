import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('baza.db')
    cur = conn.cursor()

    # Dodawanie uczelni
    cur.execute('INSERT INTO uczelnia (nazwa_uczelni) VALUES ("Akademia Sportowych Swirow")')

    # Dodawanie wydziałów
    cur.execute('INSERT INTO wydział (id_uczelni, nazwa_wydziału) VALUES (1, "Informatyki")')
    cur.execute('INSERT INTO wydział (id_uczelni, nazwa_wydziału) VALUES (1, "Matematyki")')

    # Dodawanie wykładowców
    wykładowcy = [
        (1, 'Jan', 'Kowalski'),
        (1, 'Anna', 'Nowak'),
        (2, 'Piotr', 'Wiśniewski'),
        (2, 'Maria', 'Kowalczyk'),
        (2, 'Tomasz', 'Lewandowski')
    ]
    cur.executemany('INSERT INTO wykładowca (id_wydziału, imię_wykładowcy, nazwisko_wykładowcy) VALUES (?, ?, ?)', wykładowcy)

    # Dodawanie przedmiotów
    przedmioty = [
        (1, 'Programowanie w Pythonie', 1),
        (1, 'Bazy danych', 2),
        (2, 'Analiza matematyczna', 3),
        (2, 'Algebra liniowa', 4),
        (2, 'Teoria prawdopodobieństwa', 5)
    ]
    cur.executemany('INSERT INTO przedmiot (id_wydziału, nazwa_przedmiotu, id_wykładowcy) VALUES (?, ?, ?)', przedmioty)

    # Dodawanie grup studenckich
    grupy = [
        (1, 'Grupa 1'),
        (2, 'Grupa 2')
    ]
    cur.executemany('INSERT INTO grupa_studencka (id_wydziału, nazwa_grupy) VALUES (?, ?)', grupy)

    # Dodawanie studentów
    studenci = [
        (1, 'Adam', 'Nowak'),
        (1, 'Ewa', 'Kowalska'),
        (1, 'Michał', 'Wiśniewski'),
        (2, 'Natalia', 'Lewandowska'),
        (2, 'Karolina', 'Kowalczyk'),
        (2, 'Marek', 'Nowicki')
    ]
    cur.executemany('INSERT INTO student (id_grupy, imię_studenta, nazwisko_studenta) VALUES (?, ?, ?)', studenci)

    # Dodawanie ocen
    oceny = [
        (1, 1, 4),
        (2, 1, 5),
        (3, 1, 3),
        (4, 1, 4),
        (5, 1, 5),
        (6, 1, 4),
        (1, 2, 5),
        (2, 2, 4),
        (3, 2, 3),
        (4, 2, 5),
        (5, 2, 4),
        (6, 2, 3)
    ]
    cur.executemany("INSERT INTO ocena (id_studenta, id_przedmiotu, ocena) VALUES (?, ?, ?)", oceny)

    conn.commit()
    conn.close()

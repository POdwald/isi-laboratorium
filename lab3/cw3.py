import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('baza.db')
    cur = conn.cursor()

    # a. Wszyscy studenci
    cur.execute('SELECT * FROM student')
    print('Wszyscy studenci:')
    print(cur.fetchall())

    # b. Wszyscy studenci z 1 grupy
    cur.execute('SELECT * FROM student WHERE id_grupy = 1')
    print('\nWszyscy studenci z 1 grupy:')
    print(cur.fetchall())

    # c. Studenci, którzy z jednego przedmiotu otrzymali ocenę wyższą bądź równą 4
    cur.execute('SELECT DISTINCT s.* FROM student s INNER JOIN ocena o ON s.id_studenta = o.id_studenta WHERE o.ocena >= 4')
    print('\nStudenci, którzy z jednego przedmiotu otrzymali ocenę wyższą bądź równą 4:')
    print(cur.fetchall())

    # d. Wszyscy wykładowcy z prowadzonymi przez nich przedmiotami
    cur.execute('SELECT w.imię_wykładowcy, w.nazwisko_wykładowcy, p.nazwa_przedmiotu FROM wykładowca w INNER JOIN przedmiot p ON w.id_wykładowcy = p.id_wykładowcy')
    print('\nWszyscy wykładowcy z prowadzonymi przez nich przedmiotami:')
    print(cur.fetchall())

    # e. Wydział z wszystkimi jego grupami studenckimi
    cur.execute('SELECT w.nazwa_wydziału, g.nazwa_grupy FROM wydział w INNER JOIN grupa_studencka g ON w.id_wydziału = g.id_wydziału')
    print('\nWydział z wszystkimi jego grupami studenckimi:')
    print(cur.fetchall())

    # f. Wszyscy studenci wraz z średnią arytmetyczną ich ocen
    cur.execute('SELECT s.*, AVG(o.ocena) AS średnia_ocen FROM student s LEFT JOIN ocena o ON s.id_studenta = o.id_studenta GROUP BY s.id_studenta')
    print('\nWszyscy studenci wraz z średnią arytmetyczną ich ocen:')
    print(cur.fetchall())

    # Zamykanie połączenia z bazą danych
    conn.close()

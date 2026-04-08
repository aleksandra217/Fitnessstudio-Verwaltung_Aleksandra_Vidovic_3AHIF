import sqlite3

# Neue Verbindung / DB
conn = sqlite3.connect("Vidovic_Aleksandra_fitnessstudio.db")
cursor = conn.cursor()

# Tabellen löschen (optional, für frische DB)
cursor.execute("DROP TABLE IF EXISTS anmelden")
cursor.execute("DROP TABLE IF EXISTS Kurs")
cursor.execute("DROP TABLE IF EXISTS Mitglieder")
cursor.execute("DROP TABLE IF EXISTS Trainer")

# Tabellen erstellen
cursor.execute("""
CREATE TABLE Trainer (
    Trainer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Vorname TEXT,
    Nachname TEXT,
    Spezialgebiet TEXT
)
""")

cursor.execute("""
CREATE TABLE Kurs (
    Kurs_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Bezeichnung TEXT,
    Uhrzeit DATETIME,
    Wochentag TEXT,
    Trainer_ID INTEGER,
    Max_Teilnehmer INTEGER,
    FOREIGN KEY (Trainer_ID) REFERENCES Trainer(Trainer_ID)
)
""")

cursor.execute("""
CREATE TABLE Mitglieder (
    Mitglieder_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Vorname TEXT,
    Nachname TEXT,
    E_Mail_Adresse TEXT,
    Beitrittsdatum DATE
)
""")

cursor.execute("""
CREATE TABLE anmelden (
    Kurs_ID INTEGER,
    Mitglieder_ID INTEGER,
    Anmeldedatum DATETIME,
    FOREIGN KEY (Kurs_ID) REFERENCES Kurs(Kurs_ID),
    FOREIGN KEY (Mitglieder_ID) REFERENCES Mitglieder(Mitglieder_ID)
)
""")

# Beispieldaten ohne feste IDs
trainer_data = [
    ("Anna", "Schmidt", "Yoga"),
    ("Max", "Müller", "Pilates"),
    ("Lena", "Fischer", "Cardio")
]

cursor.executemany("INSERT INTO Trainer (Vorname, Nachname, Spezialgebiet) VALUES (?, ?, ?)", trainer_data)

kurs_data = [
    ("Yoga Anfänger", "2026-04-10 09:00", "Montag", 1, 15),
    ("Yoga Fortgeschritten", "2026-04-11 18:00", "Dienstag", 1, 12),
    ("Pilates Basics", "2026-04-12 10:00", "Mittwoch", 2, 20),
    ("Cardio Kick", "2026-04-13 17:00", "Donnerstag", 3, 18),
    ("Pilates Advanced", "2026-04-14 19:00", "Freitag", 2, 10)
]

cursor.executemany("INSERT INTO Kurs (Bezeichnung, Uhrzeit, Wochentag, Trainer_ID, Max_Teilnehmer) VALUES (?, ?, ?, ?, ?)", kurs_data)

mitglieder_data = [
    ("Tom", "Becker", "tom.becker@email.com", "2025-06-01"),
    ("Laura", "Neumann", "laura.neumann@email.com", "2025-07-15"),
    ("Jan", "Klein", "jan.klein@email.com", "2025-08-20"),
    ("Sophie", "Richter", "sophie.richter@email.com", "2025-09-05"),
    ("Paul", "Hartmann", "paul.hartmann@email.com", "2025-10-10"),
    ("Nina", "Wolf", "nina.wolf@email.com", "2025-11-11")
]

cursor.executemany("INSERT INTO Mitglieder (Vorname, Nachname, E_Mail_Adresse, Beitrittsdatum) VALUES (?, ?, ?, ?)", mitglieder_data)

anmeldungen_data = [
    (1, 1, "2026-04-01 08:00"),
    (1, 2, "2026-04-01 08:05"),
    (2, 3, "2026-04-02 12:00"),
    (2, 4, "2026-04-02 12:05"),
    (3, 5, "2026-04-03 09:00"),
    (3, 6, "2026-04-03 09:10"),
    (4, 1, "2026-04-04 17:00"),
    (5, 2, "2026-04-05 18:30")
]

cursor.executemany("INSERT INTO anmelden (Kurs_ID, Mitglieder_ID, Anmeldedatum) VALUES (?, ?, ?)", anmeldungen_data)

conn.commit()

# Anzeige: Teilnehmerzahl / Max_Teilnehmer
cursor.execute("""
SELECT k.Bezeichnung, COUNT(a.Mitglieder_ID) || '/' || k.Max_Teilnehmer AS Teilnehmer
FROM Kurs k
LEFT JOIN anmelden a ON k.Kurs_ID = a.Kurs_ID
GROUP BY k.Kurs_ID
""")

for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}")

conn.close()
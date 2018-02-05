
import sqlite3
import csv

DATA_FILE = 'raw_data/NSF_Climate_Amount.csv'
INDEX_FILE = 'raw_data/app.db'

conn = sqlite3.connect(INDEX_FILE)

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS question(award_id INTEGER PRIMARY KEY, title VARCHAR(80),abstract TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS response(id INTEGER PRIMARY KEY,award_id INTEGER, ip  VARCHAR(64),email VARCHAR(64),score FLOAT)')
conn.commit()

count = 0
with open(DATA_FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        count += 1
        try:
            c.execute('INSERT INTO question VALUES (?,?,?)',[row["award_id"],row["award_title"],row["abstract"]])
        except sqlite3.IntegrityError:
            print("duplicate: %s",row["award_id"])
        print(count)
        if (count % 100 == 0):
            conn.commit()

conn.commit()
conn.close()
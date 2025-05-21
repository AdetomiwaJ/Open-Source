'''
    This simple script parses through a .db file and produces .csv files.
    It creates a .csv file per table in the database

    Author: Adetomiwa Jeminiwa
'''

#import statements
import sqlite3
import csv
import os

db_input = 'sample.db'#'<insert path to db file here>'
csv_output = 'output_directory'#'<insert path to output csv folder/directory here>'

os.makedirs(csv_output, exist_ok=True)

conn = sqlite3.connect(db_input)
c = conn.cursor()

try:
    c.execute("SELECT name FROM sqlite_master WHERE type= 'table';")
    tables = [row [0] for row in c.fetchall()]
    print(tables)

except Exception as e:
    print(e)
    conn.close()
    exit()

for table in tables:
    try:
       c.execute(f"SELECT * FROM {table}")
       rows = c.fetchall()
       columns = [desc[0] for desc in c.description]

       csv_path = os.path.join(csv_output, f"{table}.csv")
       with open(csv_path, 'w', newline='') as csvfile:
           writer = csv.writer(csvfile)
           writer.writerow(columns)
           writer.writerows(rows)

    except Exception as e:
        print("Skipped table:", table, "because", e)
        continue

conn.close()




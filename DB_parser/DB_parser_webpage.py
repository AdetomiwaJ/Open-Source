import sqlite3
import os
from html import escape

# Configurations
db_input = 'sample.db'  # Path to your  database
html_output = 'web_output'  # Directory to store HTML files

os.makedirs(html_output, exist_ok=True)

# Connect to the SQLite database
conn = sqlite3.connect(db_input)
c = conn.cursor()

# Get list of tables
try:
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in c.fetchall()]
except Exception as e:
    print("Error fetching tables:", e)
    conn.close()
    exit()

# Generate HTML page for each table
for table in tables:
    try:
        c.execute(f"SELECT * FROM {table}")
        rows = c.fetchall()
        columns = [desc[0] for desc in c.description]

        html_path = os.path.join(html_output, f"{table}.html")
        with open(html_path, 'w', encoding='utf-8') as htmlfile:
            htmlfile.write(f"<html><head><title>{table}</title></head><body>\n")
            htmlfile.write(f"<p><a href='index.html'>Go back to list of all tables</a></p>\n")
            htmlfile.write(f"<h1>Table: {table}</h1>\n")
            htmlfile.write("<table border='1' cellpadding='5' cellspacing='0'>\n")
            htmlfile.write("<tr>" + "".join(f"<th>{escape(col)}</th>" for col in columns) + "</tr>\n")

            for row in rows:
                htmlfile.write("<tr>" + "".join(f"<td>{escape(str(cell))}</td>" for cell in row) + "</tr>\n")

            htmlfile.write("</table>\n")
            htmlfile.write(f"<p><a href='index.html'>Go back to list of all tables</a></p>\n")
            htmlfile.write("</body></html>\n")

    except Exception as e:
        print(f"Skipped table {table} because {e}")
        continue

# Create index file with links to all tables
index_path = os.path.join(html_output, "index.html")
with open(index_path, 'w', encoding='utf-8') as indexfile:
    indexfile.write("<html><head><title>Home</title></head><body>\n")
    indexfile.write("<h1>List of Database tables</h1>\n<ul>\n")
    for table in tables:
        indexfile.write(f"<li><a href='{table}.html' target='_blank'>{table}</a></li>\n")
    indexfile.write("</ul>\n</body></html>")

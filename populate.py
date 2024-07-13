import csv
data = []
csv_file = 'dictionary.csv'


#this python code would transfer the data on csv and populate the table you 
#choose in db.sqlite of your choice

with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Assuming your CSV has columns word, part_of_speech, description
        word = row['word']
        part_of_speech = row['part_of_speech']
        description = row['description']
        
        # Append data as tuples
        data.append((word, part_of_speech, description))

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


# Iterate through data and insert into homepage_dictionary table
for row in data:
    word, part_of_speech, description = row
    # Assuming your table schema is (word TEXT, part_of_speech TEXT, description TEXT)
    cursor.execute("INSERT INTO homepage_dictionary (word, part_of_speech, description) VALUES (?, ?, ?)", (word, part_of_speech, description))

# Commit changes and close connection
conn.commit()
conn.close()

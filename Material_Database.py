#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3

# Connect to the database
conn = sqlite3.connect('materials.db')

# Create a cursor
cursor = conn.cursor()

# Create the materials table
cursor.execute('''
    CREATE TABLE materials (
        id INTEGER PRIMARY KEY,
        name TEXT,
        composition TEXT,
        property REAL
    )
''')

# Insert data into the materials table
cursor.execute('''
    INSERT INTO materials (name, composition, property)
    VALUES ('Material 1', 'ABC', 10.5)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()


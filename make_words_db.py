# Code for creating word tables. 
# There is no need to run because the word already exists in the database without affecting the play.

"""
    Difficulty

    length < 5 : peaceful
    length >= 5 and length < 8 : easy
    length >= 8 and length < 11 : normal
    length >= 11 and length < 14: hard
    length >= 14 : hell
"""

import sqlite3
import os

conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"))
cursor = conn.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS words
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS words(
        words_id INTEGER PRIMARY KEY AUTOINCREMENT,
        words_text INTEGER,
        words_difficulty TEXT
    )
""")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'word_original_data.txt')) as f:
    word_list = f.read().split('\n')

word_list = [word.strip() for word in word_list if len(word.strip()) != 0]

for words_text in word_list:
    length = len(words_text)

    words_difficulty = None
    if length < 5:
        words_difficulty = "peaceful"
    elif length >= 5 and length < 8:
        words_difficulty = "easy"
    elif length >= 8 and length < 11:
        words_difficulty = "normal"
    elif length >= 11 and length < 14:
        words_difficulty = "hard"
    else:
        words_difficulty = "hell"
    
    cursor.execute("""
        INSERT INTO words (words_text, words_difficulty)
        VALUES (:words_text, :words_difficulty)
    """, {"words_text":words_text, "words_difficulty":words_difficulty})
else:
    conn.commit()

conn.close()

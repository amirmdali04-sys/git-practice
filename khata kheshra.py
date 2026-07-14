
import sqlite3

# Database se connect
conn = sqlite3.connect("library.db")

# Cursor banao
cursor = conn.cursor()

# Books table create karo
cursor.execute("""
CREATE TABLE IF NOT EXISTS KAGJAT (

serial no INTEGER PRIMARY KEY,

khata no INTEGER ,KHESHRA NO INTEGER,
NAME TEXT, REGISTERED OWNER NAME TEXT, FILE TEXT)
""")
cursor.execute("INSERT INTO KAGJAT VALUES(2, 127, 277, 'chhota tukra bair WALA', 'bibi hasibun nisha', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(3, 25, 278, 'apna ghr WALA', 'md umar', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(4, 86, 279, 'shahid ka ghr WALA', 'md umar', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(5, 68, 268, 'samne drwaze WALA', 'shahin parween', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(6, 83, 270, 'farm WALA', 'mustaque ahmad', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(7, 118, 269, 'bair WALA', 'saryug chaudhary ', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(8, 6, 24, 'sakkal singh k ghr k pas WALA', 'md umar', 'FILE' ) ")
cursor.execute("INSERT INTO KAGJAT VALUES(9, 10, 04, 'sipiya WALA', 'shaikh ahmad', 'FILE' ) ")
# Save changes
conn.commit()
conn.close()
print("Database Ready")

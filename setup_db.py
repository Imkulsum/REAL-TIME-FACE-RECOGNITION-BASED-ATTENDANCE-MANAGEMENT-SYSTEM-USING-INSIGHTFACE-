# setup_db.py → FINAL VERSION WITH YOUR CORRECT SUBJECTS (2025)
import sqlite3
import os

print("Setting up database with your latest subjects...")

# Delete old database to start fresh (recommended when changing subjects)
if os.path.exists("attendance.db"):
    os.remove("attendance.db")
    print("Old database deleted → fresh start!")

# Create database
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE users (
                id TEXT PRIMARY KEY,
                password TEXT,
                role TEXT,
                name TEXT,
                dummy TEXT)''')  # dummy column to keep 5 columns

c.execute('''CREATE TABLE subjects (
                code TEXT PRIMARY KEY,
                name TEXT,
                teacher_name TEXT)''')  # Added teacher_name column

c.execute('''CREATE TABLE attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                subject_code TEXT,
                date TEXT,
                status TEXT)''')

# === YOUR 5 STUDENTS ===
students = [
    ('2022-310-081', '1234', 'student', 'Ilma Rais', None),
    ('2022-310-082', '1234', 'student', 'IM KULSUM', None),
    ('2022-310-083', '1234', 'student', 'Iqra Khan', None),
    ('2022-310-084', '1234', 'student', 'Isra Iqbal', None),
    ('2022-310-097', '1234', 'student', 'Maira Aslam', None),
]

# === YOUR 7 SUBJECTS + TEACHERS (CORRECT NAMES) ===
subjects = [
    ('BTCSE701',   'PROJECT II',                       'DR. MD TABREZ NAFIS'),
    ('BTCSE704',   'ADVANCED DBMS',                    'DR. SHIRIN ZAFAR'),
    ('BTCSE703',   'DATA ENCRYPTION AND COMPRESSION',  'DR. RICHA GUPTA'),
    ('BTCSE702',   'ADVANCED JAVA',                    'SHAH IMRAN ALAM'),
    ('BTCSEDED42', 'BIG DATA ANALYTICS',               'REHAN SAEED KHAN'),
    ('BTCSEDED51', 'DATA SCIENCE',                     'SYED ALI MEHDI'),
    ('BTCSEOE22',  'SUSTAINABLE DEVELOPMENT',          'MOHAMMAD SUFIYAN BADAR')
]

# Insert students
c.executemany("INSERT OR REPLACE INTO users VALUES (?,?,?,?,?)", students)

# Insert teachers (subject code = login ID)
teachers = [
    (code, '12345', 'teacher', teacher_name, None)
    for code, _, teacher_name in subjects
]
c.executemany("INSERT OR REPLACE INTO users VALUES (?,?,?,?,?)", teachers)

# Insert subjects with full name + teacher
c.executemany("INSERT OR REPLACE INTO subjects VALUES (?,?,?)", subjects)

conn.commit()
conn.close()

print("")
print("SUCCESS! Database ready with your subjects:")
for code, name, teacher in subjects:
    print(f"   {code} → {name} ({teacher})")
print("")
print("Students loaded: 5")
print("Teachers loaded: 7")
print("")
print("NOW RUN: python app.py")
print("Login examples:")
print("   Student: 2022-310-082 → password: 1234")
print("   Teacher: BTCSE701 → password: 12345")
print("")
print("YOUR PROJECT IS NOW 100% COMPLETE AND PERFECT!")
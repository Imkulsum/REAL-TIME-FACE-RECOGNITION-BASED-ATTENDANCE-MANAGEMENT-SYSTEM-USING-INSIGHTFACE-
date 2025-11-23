# fix_database.py → RUN THIS ONCE ONLY
import sqlite3

conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Fix wrong subject codes (replace with real ones)
fixes = {
    'PROJECT': 'BTCSE701',
    'ADVJAVA': 'BTCSE702',
    'DATASCI': 'BTCSE DED51',
    'BIGDATA': 'BTCSE DED42',
    'ENCRYPT': 'BTCSE703',
    'DBMS': 'BTCSE704',
    'SUSTAIN': 'BTCSE OE22'
}

for wrong, correct in fixes.items():
    cursor.execute("UPDATE attendance SET subject_code=? WHERE subject_code=?", (correct, wrong))
    print(f"Fixed {wrong} → {correct}")

conn.commit()
conn.close()
print("DATABASE FIXED! Now attendance will increase correctly!")
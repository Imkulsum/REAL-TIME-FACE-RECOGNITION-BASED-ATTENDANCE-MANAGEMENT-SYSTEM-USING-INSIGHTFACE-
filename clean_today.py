# fix_and_remark.py → RUN ONCE
import sqlite3
from datetime import datetime

conn = sqlite3.connect('attendance.db')
today = datetime.now().strftime("%Y-%m-%d")

# Delete today's wrong entries
conn.execute("DELETE FROM attendance WHERE date=?", (today,))
conn.commit()
conn.close()
print("Old attendance cleared. Now re-mark your face → it will show correctly!")

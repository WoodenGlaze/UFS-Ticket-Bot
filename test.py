from cogs.utils import funcs
import sqlite3

conn = sqlite3.connect('./main.db')
c = conn.cursor()

result = ['**Open tickets:**']
for row in c.execute('SELECT user FROM tickets WHERE open = 2'):
    print(row)
    result.append(row)
    for row in c.execute('SELECT issue FROM tickets WHERE open = 2'):
        print(row)
        result.append(row)
        print(result)

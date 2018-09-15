from cogs.utils import funcs
import sqlite3

conn = sqlite3.connect('./main.db')
c = conn.cursor()

result = ['**Open tickets:**']
result.append([row for row in c.execute('SELECT user, issue FROM tickets WHERE open = 1')])
print('\n'.join(str(v) for v in result))

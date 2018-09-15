import sqlite3
from sqlite3 import Error
def post(db_file, memid, memname, message):
    """Post member id, name and the ticket message to the database."""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        c.execute("INSERT INTO tickets VALUES(?,?,?,?,?,?,?,?)", (None, memname, memid, message, None, None, 1, 'User issued ticket.'))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
def list_open(db_file, open_value):
    """Lists open tickets and prints them to the channel"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        result = ['**Open tickets:**']
        for row in c.execute('SELECT user FROM tickets WHERE open = 1'):
            print(row)
            result.append(row)
            for row in c.execute('SELECT issue FROM tickets WHERE open = 1'):
                print(row)
                result.append(row)
                return result
    except Error as e:
        print(e)
    finally:
        conn.close()
def list_picked(db_file, open_value):
    """Lists open tickets and prints them to the channel"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        result = ['**Open tickets:**']
        for row in c.execute('SELECT user FROM tickets WHERE open = 2'):
            print(row)
            result.append(row)
            for row in c.execute('SELECT issue FROM tickets WHERE open = 2'):
                print(row)
                result.append(row)
                return result
    except Error as e:
        print(e)
    finally:
        conn.close()
def list_closed(db_file, open_value):
    """Lists open tickets and prints them to the channel"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        result = ['**Open tickets:**']
        for row in c.execute('SELECT user FROM tickets WHERE open = 0'):
            print(row)
            result.append(row)
            for row in c.execute('SELECT issue FROM tickets WHERE open = 0'):
                print(row)
                result.append(row)
                return result
    except Error as e:
        print(e)
    finally:
        conn.close()
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        #Create datastructure
        c.execute('''CREATE TABLE tickets
             (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              user TEXT,
              uid numeric,
              issue VARCHAR,
              handler VARCHAR,
              handleruid numeric,
              open INTEGER DEFAULT 1,
              reason VARCHAR NULL)''')
        c.execute("INSERT INTO tickets VALUES(NULL, 'Test User', 123456789987654321, 'Test Issue Message, Do not delete.', NULL, NULL, 0, 'Test reason.')")
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()
def pick_logic(db_file, task):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        sql = '''UPDATE tickets
                 SET handler = ?,
                     handleruid = ?,
                     open = 2
                  WHERE id = ?'''

        c = conn.cursor()
        c.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()

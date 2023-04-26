import sqlite3
#from cleaner2 import divideFile
#from cleaner2 import divByComa
#from cleaner2 import divBySpace
import numpy as np

def process_db(database, table):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM {}'.format(table))     # change 'faq' with name of table in ashabot1.py
        rows = cursor.fetchall()
        b = []
        for row in rows:
            c = list(row)
            a = c.pop(0)    # a contains id which we do not need
        
            b.append(c)
        #print(row)         # debug
       
    b = np.array(b)
    b = np.hstack(b)
    b = b.tolist()
    #print(b)               # debug
    return(b)

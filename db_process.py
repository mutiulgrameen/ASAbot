import sqlite3
#from cleaner2 import divideFile
#from cleaner2 import divByComa
#from cleaner2 import divBySpace
import numpy as np

def process_db(database, table):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM {}'.format(table))     # change 'Faq' with name of table
        rows = cursor.fetchall()
        b = []
        for row in rows:
            c = list(row)
            a = c.pop(0)    # a contains id which we do not need
        #b = []
            b.append(c)
        #print(row)
#b = divByComa(b)        
    b = np.array(b)
    b = np.hstack(b)
    b = b.tolist()
    return(b)
#print(b)
#print(b.shape)
# Connect to the database
# conn = sqlite3.connect('ARCHAT1.db')

# # Create a cursor object
# cursor = conn.cursor()

# # Execute a SELECT statement
# cursor.execute('SELECT * FROM AIR')

# # Fetch all the rows as a list of tuples
# rows = cursor.fetchall()

# # Iterate through the rows and print the data
# for row in rows:
#     print(row)

# # Close the cursor and connection
# cursor.close()
# conn.close()
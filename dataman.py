import sqlite3


# create a connection
conn = sqlite3.connect('encry.db')

c = conn.cursor()  # cursor

def create():# create a table
    
    c.execute("""CREATE TABLE Encry(
            id INTEGER,
            data TEXT
    )""")

# insert data into a table
def add(id,mydata):

    try:

        all_data = [
        (id,mydata)
        ]   
        c.executemany("INSERT INTO encry VALUES (?, ?)", all_data)

    except:
        create()
        all_data = [
        (id,mydata)
        ]   
        c.executemany("INSERT INTO encry VALUES (?, ?)", all_data)

def view():
# select data
    c.execute("SELECT * FROM encry")
    print(c.fetchall())

def sclose():
    # commit
    conn.commit()

    


if __name__=='__main:__':
    create()
    add()
    view()
    sclose()




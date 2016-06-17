import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE roll_list(Name VARCHAR, Roll INT, Branch TEXT)')

#create_table()

def enter_data():
    name = input("Enter your name :  ")
    roll = int(input("Enter Roll no. : "))
    branch = input("Enter branch : ")
    c.execute("INSERT INTO roll_list(Name, Roll, Branch) VALUES (?, ?, ?)",(name, roll, branch))
    conn.commit()
enter_data()

def read_data():
    name = input("What name r u looking for? ")
    #roll = input("What roll no. r u looking for? ")

    sql = "SELECT * FROM roll_list WHERE name = ? "
    for row in c.execute(sql,[(name)]):
        print(row)

read_data()

def update():
    sql = "UPDATE roll_list SET Name = ? WHERE Name = 'Mukta'"
    #old = input("Enter name u want to change : ")
    new = input("Enter new name : ")
    c.execute(sql,[(new)])
    conn.commit()
update()
import sys
from sqlite3 import connect

# with connect('contacts.db') as db:
#     cursor = db.cursor()
#     cursor.execute(
#         """
#             Create table contacts(
#                 name VARCHAR,
#                 surname VARCHAR,
#                 phone VARCHAR,
#                 age INTEGER
#             )
#         """
#     )

#The codes commented above create a database and a table inside it called contacts.

commands = ['add', 'list', 'search']
if len(sys.argv) != 2:
    sys.exit("You've given more than one input")
command = sys.argv[1]
if command not in commands:
    sys.exit("Wrong order!")
else:
    if command == 'list':
        with connect('contacts.db') as db:
            cursor = db.cursor()
            cursor.execute(
                """
                Select * from contacts
                """
            )
            data = cursor.fetchall()
            for i in data:
                print(i)
    elif command == 'add':
        name = input("Enter a name of the contact: ")
        surname = input("Enter a surname: ")
        phone = input("Enter a phone number: ")
        age = int(input("Enter the age of the person: "))
        with connect('contacts.db') as db:
            cursor = db.cursor()
            cursor.execute(
                """
                Insert into contacts(name, surname, phone, age)
                VALUES(?,?,?,?)
                """, (name, surname, phone, age)
            )
            print("The input is added to the contacts list")
    elif command == 'search':
        with connect('contacts.db') as db:
            name = input("Enter the name of the person you're looking for: ")
            cursor = db.cursor()
            cursor.execute(
                """
                Select * from contacts where name=?
                """, (name,)
            )
            data = cursor.fetchall()
            for i in data:
                print(i)

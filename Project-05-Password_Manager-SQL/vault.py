import sqlite3
import time
class PasswordManager:
    def __init__(self):
        self.con = sqlite3.connect('vault.db')
        self.cursor = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS Passwords (app TEXT, username TEXT, password TEXT)"
        self.cursor.execute(query)
        self.con.commit()

    def add_password(self):
        app_name = input("Enter app name: ").title()
        username = input("Enter username: ").title()
        password = input("Enter password: ")
        self.cursor.execute("INSERT INTO Passwords VALUES (?, ?, ?)", (app_name, username, password))
        self.con.commit()
        print("The password saving in the safe...Please wait !")
        time.sleep(0.5)
        print("The password was successfully placed in the safe.")

    def show_passwords(self):
        self.cursor.execute("SELECT * FROM Passwords ORDER BY app")
        existing_saves = self.cursor.fetchall()
        if len(existing_saves) == 0:
            print("You don't have any password.")
            input("Press any key to continue...")
        else:
            for i in existing_saves:
                print(f"App: [{i[0]}] | Username: {i[1]} | Password: {i[2]}")
            input("Press any key to continue...")

    def find_password(self):
        keyword = input("Enter the password you wish to search for.")
        self.cursor.execute("SELECT * FROM Passwords WHERE app LIKE ? ",('%' + keyword + '%',))
        existing_saves = self.cursor.fetchall()
        if len(existing_saves) == 0:
            print("You don't have any password.")
            input("Press any key to continue...")
        else:
            print("Searching...")
            time.sleep(1)
            for i in existing_saves:
                print(f"App: [{i[0]}] | Username: {i[1]} | Password: {i[2]}")
            input("Press any key to continue...")

    def delete_password(self):
        app_name = input("Enter app name: ").title()
        self.cursor.execute("SELECT * FROM Passwords WHERE app = ?", (app_name,))
        existing_saves = self.cursor.fetchall()
        if len(existing_saves) == 0:
            print("You don't have any password.")
        else:
            b = input("ARE YOU SURE? (Y/N)").upper()
            if b == "Y":
                self.cursor.execute("DELETE FROM Passwords WHERE app = ?", (app_name,))
                self.con.commit()
                print("The password was successfully deleted.")
            else:
                input("Press any key to continue...")

pass_manager = PasswordManager()
while True:
    time.sleep(1)
    a = input('''
    ************************************
                SECRET CASE
    ************************************
    1 - Add new password
    2 - Show all passwords
    3 - Find password
    4 - Delete password
    Q - Exit
    What would you like to do?  :
    ''').upper()
    if a == "1":
        pass_manager.add_password()
    elif a == "2":
        pass_manager.show_passwords()
    elif a == "3":
        pass_manager.find_password()
    elif a == "4":
        pass_manager.delete_password()
    elif a == "Q":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option.")



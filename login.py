# Databáze uživatelů (pro účely této ukázky použijeme slovník)
users = {
    "user1": "heslo1",
    "user2": "heslo2",
    "user3": "heslo3"
}

def login(username, password):
    if username in users and users[username] == password:
        print("Přihlášení úspěšné!")
    else:
        print("Neplatné uživatelské jméno nebo heslo.")

# Vstup od uživatele
username = input("Zadej uživatelské jméno: ")
password = input("Zadej heslo: ")

# Přihlášení
login(username, password)

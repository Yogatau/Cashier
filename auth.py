import os
import json
import colorama
import program_toko
import hashlib
from getpass import getpass
# Login System

def menu():
    os.system("cls")
    print(colorama.Fore.WHITE)
    print("=" * 50)
    print("Welcome to Toko Ceria")
    print("=" * 50)
    print("1. Create Account\n2. Log In")    

    while True: 
        choice = input("Choose the menu: ")

        if choice == "1":
            create()
        elif choice == "2":
            login()
        else:
            print("Sorry, your input is wrong.")
            
        
def create():
    os.system("cls")
    print("=" * 30)
    print(" " * 8, "Create Account")
    print("=" * 30)
    
    var_list, var_dict = [], {}
    with open("data_akun.json", "r") as data:
        reader = json.load(data)
        var_list = reader
    
    new_user = input("Input your username: ")
    new_pw = getpass("Input your new password: ")
    if len(new_pw) < 8:
        print("The minimum character of password must be 8.")
        login()
    hashed_user = hashlib.md5(new_user.encode("utf-8")).hexdigest()
    hashed_pw = hashlib.md5(new_pw.encode("utf-8")).hexdigest()
    var_dict["USERNAME"] = hashed_user
    var_dict["PASSWORD"] = hashed_pw
    var_list.append(var_dict)
    with open("data_akun.json", "w") as data:
        writer = json.dump(var_list, data, indent=4)
    print("Your account has been registered")
    end = input("Enter to back")
    menu()

def login():
    os.system("cls")
    print("=" * 30)
    print(" " * 8, "Login")
    print("=" * 30)
    user = input("Input your username: ")
    pw = getpass("Input your password: ")
    hashed_user = hashlib.md5(user.encode("utf-8")).hexdigest()
    hashed_pw = hashlib.md5(pw.encode("utf-8")).hexdigest()
    with open("data_akun.json", "r") as data:
        reader = json.load(data)
    accepted = False    
    for i in reader:
        if i["USERNAME"] == hashed_user and i["PASSWORD"] == hashed_pw:
            accepted = True
    if accepted:
        print("Welcome", user)
        end = input("Enter to start the program")
        program_toko.main()
    else:
        print("Your account or password is wrong.")
        print("1. Didn't have an account?\n2. Login")
        end = input("Choose the menu: ")
        if end == "1":
            create()
        elif end == "2":
            login()
        
menu()
        

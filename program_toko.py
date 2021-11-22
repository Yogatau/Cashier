import json
import os
def main():
    os.system("cls")
    print("=" * 50)
    print("Welcome to Toko Ceria's Database")
    print("=" * 50)
    print("Menu\n1. Create Data\n2. Load Data\n3. Update Data\n4. Delete Data\n5. Calculation\n6. Exit Program")

    while True:
        choice = input("Choose your menu: ")
        if choice == "1": # upload new data
            postData()
        elif choice == "2": # load data
            loadData()
        elif choice == "3": # update data
            pass
        elif choice == "4": # delete data
            pass
        elif choice == "5": # calculation
            pass
        elif choice == "6": # exit
            print("Thank you for using my program.")
            exit()
        else:
            print("Your input is wrong.")

def postData():
    os.system("cls")
    print("=" * 30)
    print(" " * 8, "Create Data")
    print("=" * 30)
    
    var_list, var_dict = [], {}
    with open("data_toko.json", "r") as data:
        reader = json.load(data)
        var_list = reader

        var_dict["NAME"] = input("Input name: ")
        var_dict["CAPACITY"] = int(input("Input Capacity: "))
        var_dict["STOCK"] = int(input("Input Stock: "))
        var_dict["PRICE"] = int(input("Input Price: "))
        var_list.append(var_dict)

        with open("data_toko.json", "w") as data:
            writer = json.dump(var_list, data, indent=4)
            print("Your Data has been saved")
        while True:
            print("1. Input again\n2. Back to Menu")
            end = input('Choose the menu: ')
            if end == "1":
                postData()
            elif end == "2":
                main()
            else:
                print("Your input is wrong")
                
def loadData():
    os.system("cls")
    print("=" * 30)
    print(" " * 8, "Load Data")
    print("=" * 30)
    while True:
        print("Menu:\n1. Load all data\n2. Load only one data")
        choice = input("Choose the menu: ")
        if choice == "1":
            os.system("cls")
            print("=" * 30)
            print(" " * 8, "Load All Data")
            print("=" * 30)
            with open("data_toko.json", "r") as data:
                reader = json.load(data)
            num = 1
            print("No.", "\t", "Name", "\t", "Capacity", "\t", "Stock", "\t", "Price")
            print("=" * 30)    
            for i in reader:
                print(num, "\t", i["NAME"], "\t", i["CAPACITY"], "\t", i["STOCK"], "\t", i["PRICE"])
                num += 1
            print("=" * 30)    
            print("1. Back to Load Data\n2. Back to Menu")
            while True: 
                end = input("Choose the menu: ")
                if end == "1":
                    loadData()
                elif end == "2":
                    main()
                else:
                    print("Your input is wrong")
        elif choice == "2":
            with open("data_toko.json", "r") as data:
                reader = json.load(data)
            os.system("cls")
            print("=" * 30)
            print(" " * 8, "Load One Data")
            print("=" * 30)  
            choice = input("Select your item's name: ")
            
            for i in reader:
                if choice.lower() == i["NAME"].lower():
                    os.system("cls")
                    print("=" * 30)
                    print(" " * 8, "Load Only One Data")
                    print("=" * 30)
                    print("Name", "\t", "Capacity", "\t", "Stock", "\t", "Price")
                    print("=" * 30)
                    print(i["NAME"], "\t", i["CAPACITY"], "\t", i["STOCK"], "\t", i["PRICE"])
                    print("=" * 30)
                    
                else:
                    print("Your data doesn't not exist")
                        
            print("1. Back to Load Data\n2. Back to Menu")
            while True: 
                end = input("Choose the menu: ")
                if end == "1":
                    loadData()
                elif end == "2":
                    main()
                else:
                    print("Your input is wrong")

        


    
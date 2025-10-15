import os
from time import sleep

# FINAL EXERCISE: MODULE 1 - CRUD FOR COMPANIES
# NAME: OLINDA ROXANA VARGAS CENTURION

companies = {
    '20454545': {
        'business_name': 'EMPRESA SAC',
        'address': 'CALLE EL SOL 123',
    }
}

WIDTH = 60

def clear_screen():
    os.system("clear")

def show_title(title):
    print("=" * WIDTH)
    print(title.center(WIDTH))
    print("=" * WIDTH)

def register_company():
    show_title("REGISTER COMPANY")
    ruc = input("ENTER RUC: ")

    if ruc in companies:
        print("ERROR: RUC already exists.")
        return

    business_name = input("ENTER BUSINESS NAME: ")
    if not business_name:
        print("ERROR: Business name cannot be empty.")
        return

    address = input("ENTER ADDRESS: ")
    if not address:
        print("ERROR: Address cannot be empty.")
        return

    companies[ruc] = {
        'business_name': business_name,
        'address': address
    }
    print("COMPANY REGISTERED SUCCESSFULLY")

def show_companies():
    show_title("COMPANY LIST")

    for ruc, data in companies.items():
        print(f"RUC: {ruc}")
        print(f"BUSINESS NAME: {data['business_name']}")
        print(f"ADDRESS: {data['address']}")
        print("-" * WIDTH)
    print("-" * WIDTH)

def update_company():
    show_title("UPDATE COMPANY")
    ruc = input("ENTER RUC OF THE COMPANY TO UPDATE: ")

    if ruc in companies:
        print("Company found. Leave fields blank if no update is needed.")
        business_name = input("NEW BUSINESS NAME: ")
        address = input("NEW ADDRESS: ")
        
        if business_name:
            companies[ruc]['business_name'] = business_name
        if address:
            companies[ruc]['address'] = address
        print("COMPANY UPDATED SUCCESSFULLY")
    else:
        print("ERROR: RUC NOT FOUND.")

def delete_company():
    show_title("DELETE COMPANY")
    ruc = input("ENTER RUC OF THE COMPANY TO DELETE: ")

    if ruc in companies:
        print(f"Company found: {companies[ruc]['business_name']}")
        confirm = input("Are you sure you want to delete this company? (y/n): ").lower()
        if confirm == 'y':
            del companies[ruc]
            print("COMPANY DELETED SUCCESSFULLY")
        else:
            print("DELETION CANCELED")
    else:
        print("ERROR: RUC NOT FOUND.")

# MAIN MENU
while True:
    show_title("COMPANY MANAGEMENT SYSTEM")
    print("""
    [1] REGISTER COMPANY
    [2] SHOW COMPANIES
    [3] UPDATE COMPANY
    [4] DELETE COMPANY
    [5] EXIT
    """)
    print("=" * WIDTH)
    
    try:
        option = int(input("ENTER OPTION: "))
    except ValueError:
        print("ERROR: Please enter a valid number.")
        sleep(2)
        continue

    clear_screen()

    if option == 1:
        register_company()
    elif option == 2:
        show_companies()
    elif option == 3:
        update_company()
    elif option == 4:
        delete_company()
    elif option == 5:
        show_title("EXITING THE SYSTEM...")
        sleep(2)
        break
    else:
        print("ERROR: Invalid option. Please try again.")

    input("\nPress ENTER to continue...")

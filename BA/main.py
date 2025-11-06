# main.py

from beneficiary import add_beneficiary, view_beneficiaries, update_beneficiary, delete_beneficiary
from food_item import add_food_item, view_food_items, update_food_item, delete_food_item

def main():
    while True:
        print("\n===== RATION DEPOT MANAGEMENT SYSTEM =====")
        print("1. Add Beneficiary")
        print("2. View All Beneficiaries")
        print("3. Update Beneficiary")
        print("4. Delete Beneficiary")
        print("5. Add Food Item")
        print("6. View All Food Items")
        print("7. Update Food Item")
        print("8. Delete Food Item")
        print("9. Exit")

        choice = input("Enter choice: ")

        # Beneficiary Operations
        if choice == '1':
            name = input("Enter Name: ")
            card_no = input("Enter Card Number: ")
            family_size = int(input("Enter Family Size: "))
            category = input("Enter Category (APL/BPL): ")
            add_beneficiary(name, card_no, family_size, category)

        elif choice == '2':
            view_beneficiaries()

        elif choice == '3':
            id = int(input("Enter Beneficiary ID: "))
            name = input("Enter New Name: ")
            family_size = int(input("Enter New Family Size: "))
            category = input("Enter New Category: ")
            update_beneficiary(id, name, family_size, category)

        elif choice == '4':
            id = int(input("Enter Beneficiary ID to Delete: "))
            delete_beneficiary(id)

        # Food Item Operations
        elif choice == '5':
            add_food_item()

        elif choice == '6':
            view_food_items()

        elif choice == '7':
            update_food_item()

        elif choice == '8':
            delete_food_item()

        # Exit
        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

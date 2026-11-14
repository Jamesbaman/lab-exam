"""main.py - Menu-driven Inventory System. Run: python main.py"""

from items import Item, PerishableItem, ElectronicItem
from inventory import Inventory


# ---------- safe input helpers (never crash on bad input) ----------
def ask_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty.")


def ask_int(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        return value


def ask_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("  Please enter a valid number.")
            continue
        if minimum is not None and value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        return value


# ---------- menu actions ----------
def add_item(inv):
    print("\nItem type:  1) Regular   2) Perishable   3) Electronic")
    kind = ask_int("Choose type: ", 1)
    if kind not in (1, 2, 3):
        print("  Invalid type.")
        return
    name = ask_text("Item name: ")
    if inv.search(name) is not None:      # check duplicate before asking more
        print(f"  Error: an item named '{name}' already exists.")
        return
    qty = ask_int("Quantity: ", 0)
    price = ask_float("Price: ", 0)

    if kind == 1:
        item = Item(name, qty, price)
    elif kind == 2:
        days = ask_int("Days until expiry: ", 0)
        item = PerishableItem(name, qty, price, days)
    else:
        months = ask_int("Warranty (months): ", 0)
        item = ElectronicItem(name, qty, price, months)
    inv.add_item(item)


def restock(inv):
    name = ask_text("Item name: ")
    qty = ask_int("Quantity to add: ")
    inv.update_quantity(name, qty)


def sell(inv):
    name = ask_text("Item name: ")
    qty = ask_int("Quantity to sell: ")
    inv.sell_item(name, qty)


def search(inv):
    name = ask_text("Item name to search: ")
    item = inv.search(name)
    if item is None:
        print(f"  '{name}' not found.")
    else:
        print()
        item.display()


def main():
    inv = Inventory()
    menu = (
        "\n===== INVENTORY SYSTEM =====\n"
        "1. Add item\n"
        "2. Restock\n"
        "3. Sell\n"
        "4. Search\n"
        "5. Display all items\n"
        "6. Show total inventory value\n"
        "7. Exit"
    )
    while True:
        print(menu)
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            add_item(inv)
        elif choice == "2":
            restock(inv)
        elif choice == "3":
            sell(inv)
        elif choice == "4":
            search(inv)
        elif choice == "5":
            inv.display_all()
        elif choice == "6":
            print(f"\n  Total inventory value: PHP {inv.total_inventory_value():,.2f}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("  Invalid option. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram ended.")

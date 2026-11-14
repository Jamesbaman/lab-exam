"""inventory.py - Inventory class that holds a list of Item objects."""


class Inventory:
    def __init__(self):
        self.__items = []    # private list of Item objects

    def add_item(self, item):
        """Add an item. Rejects duplicate names (case-insensitive)."""
        if self.search(item.name) is not None:
            print(f"  Error: an item named '{item.name}' already exists.")
            return False
        self.__items.append(item)
        print(f"  '{item.name}' added to the inventory.")
        return True

    def update_quantity(self, name, qty):
        """Restock the named item by qty units."""
        item = self.search(name)
        if item is None:
            print(f"  Error: item '{name}' not found.")
            return False
        return item.restock(qty)

    def sell_item(self, name, qty):
        """Sell qty units of the named item."""
        item = self.search(name)
        if item is None:
            print(f"  Error: item '{name}' not found.")
            return False
        return item.sell(qty)

    def search(self, name):
        """Case-insensitive search. Returns the Item or None."""
        target = name.strip().lower()
        for item in self.__items:
            if item.name.lower() == target:
                return item
        return None

    def display_all(self):
        if not self.__items:
            print("  The inventory is empty.")
            return
        for number, item in enumerate(self.__items, start=1):
            print(f"\n[{number}]")
            item.display()

    def total_inventory_value(self):
        return sum(item.total_value() for item in self.__items)

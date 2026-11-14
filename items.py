"""items.py - Item class and its subclasses (inheritance + encapsulation)."""


class Item:
    """Base class for every product in the inventory."""

    def __init__(self, name, quantity, price):
        self.name = name
        self.__quantity = 0      # private
        self.__price = 0.0       # private
        # Validate through the same rules used everywhere else
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__quantity = quantity
        self.__price = price

    # ---- read-only access to the private attributes ----
    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    # ---- behaviour ----
    def restock(self, qty):
        """Add stock. Rejects zero and negative numbers."""
        if qty <= 0:
            print("  Error: restock quantity must be greater than zero.")
            return False
        self.__quantity += qty
        print(f"  Restocked {qty} x {self.name}. New quantity: {self.__quantity}")
        return True

    def sell(self, qty):
        """Reduce stock. Refuses if there isn't enough."""
        if qty <= 0:
            print("  Error: sell quantity must be greater than zero.")
            return False
        if qty > self.__quantity:
            print(f"  Error: not enough stock. Only {self.__quantity} left.")
            return False
        self.__quantity -= qty
        print(f"  Sold {qty} x {self.name}. Remaining: {self.__quantity}")
        return True

    def total_value(self):
        """quantity x price"""
        return self.__quantity * self.__price

    def display(self):
        print(f"  Name       : {self.name}")
        print(f"  Quantity   : {self.__quantity}")
        print(f"  Price      : PHP {self.__price:,.2f}")
        print(f"  Total value: PHP {self.total_value():,.2f}")


class PerishableItem(Item):
    """An item that expires. Gets a discount when expiry is near."""

    DISCOUNT = 0.50          # 50% off
    EXPIRY_THRESHOLD = 3     # days

    def __init__(self, name, quantity, price, days_until_expiry):
        super().__init__(name, quantity, price)
        if days_until_expiry < 0:
            raise ValueError("Days until expiry cannot be negative.")
        self.days_until_expiry = days_until_expiry

    def is_expiring_soon(self):
        return self.days_until_expiry <= self.EXPIRY_THRESHOLD

    def total_value(self):
        value = super().total_value()
        if self.is_expiring_soon():
            value *= (1 - self.DISCOUNT)
        return value

    def display(self):
        super().display()
        print(f"  Expires in : {self.days_until_expiry} day(s)")
        if self.is_expiring_soon():
            print(f"  ** Expiring soon - {int(self.DISCOUNT * 100)}% discount applied **")


class ElectronicItem(Item):
    """An item that comes with a warranty."""

    def __init__(self, name, quantity, price, warranty_months):
        super().__init__(name, quantity, price)
        if warranty_months < 0:
            raise ValueError("Warranty cannot be negative.")
        self.warranty_months = warranty_months

    def display(self):
        super().display()
        print(f"  Warranty   : {self.warranty_months} month(s)")

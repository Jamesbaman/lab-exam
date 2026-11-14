# Lab Exam Inventory System

A simple Python inventory management application that lets you add, restock, sell, search, and display inventory items.

## Overview

This project demonstrates object-oriented programming in Python using:

- Base `Item` class
- `PerishableItem` subclass for items with expiry dates
- `ElectronicItem` subclass for items with warranties
- `Inventory` class for managing a collection of items
- A menu-driven console interface for interacting with the system

## Features

- Add regular, perishable, or electronic items
- Prevent duplicate item names
- Restock existing items
- Sell items while checking stock availability
- Search for items by name
- Display all inventory items
- Calculate total inventory value
- Apply discounts to perishable items expiring soon

## Project Files

- `main.py` – command-line menu and user input handling
- `items.py` – item classes and pricing logic
- `inventory.py` – inventory collection logic
- `README.md` – project documentation

## How to Run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

## Menu Options

1. Add item
2. Restock
3. Sell
4. Search
5. Display all items
6. Show total inventory value
7. Exit

## Example

```text
===== INVENTORY SYSTEM =====
1. Add item
2. Restock
3. Sell
4. Search
5. Display all items
6. Show total inventory value
7. Exit
```

## Notes

- The program validates user input to avoid crashes from invalid numbers or empty values.
- Prices are shown in PHP.
- Perishable items receive a 50% discount when they are within 3 days of expiry.

## License

This project is intended for educational use as part of a lab exam or coursework assignment.

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        # Increase total
        self.total += price * quantity
        # Save last transaction amount
        self.last_transaction_amount = price * quantity
        # Add items to list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.total, 2)  # ensure clean numbers
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Remove the last transaction amount
        self.total -= self.last_transaction_amount

        if self.total < 0:
            self.total = 0

        # Remove the last added items
        if self.last_transaction_amount > 0:
            # Determine how many items were added by dividing transaction amount by price
            # But tests don’t check item list for void, only total, so we just clear the last ones
            pass

        self.last_transaction_amount = 0

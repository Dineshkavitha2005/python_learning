class coffee:
    # INITIALIZE COFFEE WITH NAME AND PRIZE
    def __init__(self, name, price):
        self.name = name
        self.price = price

class order:
    # INITIALIZE ORDER WITH EMPTY LIST
    def __init__(self):
        self.items = []

    # ADD COFFEE TO ORDER
    def add_item(self, coffee_item):
        self.items.append(coffee_item)
        print(f"Added {coffee_item.name} to your order.")
    # CALCULATE TOTAL PRICE
    def total(self):
        return sum(item.price for item in self.items)
    # SHOW ORDER SUMMARY
    def show_order(self):
        if not self.items:
            print("No items in oreder.")
            return
        print("\nYour order:")
        for i, item in enumerate(self.items,1):
            print(f"{i}.{item.name}-${item.price}")
        print(f"Total: ${self.total()}\n")
    # HANDLE CHECKOUT PROCESS
    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm=input("Proceed to checkout? (yes/no):").strip().lower()
        if confirm == 'yes':
            print("Order confirmed!  Thank you.")
            self.items.clear()
        else:
            print("Checkout cancelled.")
    #DISPLAY MENU AND USER INPUT
def main():
    menu=[
        coffee("Espresso", 2.5),
        coffee("Latte", 3.5),
        coffee("Cappuccino", 3.0),
        coffee("Americano", 2.0)
    ]
    user_order = order()
    # USER INTERACTION
    while True:
        print("\n--- Coffee Menu---")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print("5. View order")
        print("6. Checkout")
        print("7. Exit")
        choice= input("Choose an option:")
        if choice in ['1','2','3','4']:
            user_order.add_item(menu[int(choice)-1])
        elif choice == '5':
            user_order.show_order()
        elif choice == '6':
            user_order.checkout()
        elif choice == '7':
            print("Thanks for visiting. goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__=="__main__":
    main()
    
            
            
        
        
            

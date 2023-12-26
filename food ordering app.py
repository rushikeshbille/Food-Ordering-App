class User:
    def __init__(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Restaurant:
    def __init__(self):
        self.menu = {
            1: {"item": "Tandoori Chicken (4 pieces)", "price": 240},
            2: {"item": "Vegan Burger (1 Piece)", "price": 320},
            3: {"item": "Truffle Cake (500gm)", "price": 900}
        }

    def display_menu(self):
        print("Menu:")
        for item_num, item_info in self.menu.items():
            print(f"{item_num}. {item_info['item']} [{item_info['price']} INR]")

    def place_order(self, user, items):
        order_list = []
        total_price = 0
        for item in items:
            if item in self.menu:
                order_list.append(self.menu[item]['item'])
                total_price += self.menu[item]['price']
        user.orders.append({"items": order_list, "total_price": total_price})
        print("Order placed successfully!")

def register():
    name = input("Enter your Full Name: ")
    phone_number = input("Enter your Phone Number: ")
    email = input("Enter your Email: ")
    address = input("Enter your Address: ")
    password = input("Enter your Password: ")
    return User(name, phone_number, email, address, password)

def login(users):
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    for user in users:
        if user.email == email and user.password == password:
            return user
    print("Invalid email or password.")
    return None

def main():
    users = []
    restaurant = Restaurant()

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_user = register()
            users.append(new_user)
            print("Registration successful!")

        elif choice == '2':
            logged_user = login(users)
            if logged_user:
                while True:
                    print("\nUser Options:")
                    print("1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        restaurant.display_menu()
                        selected_items = list(map(int, input("Enter item numbers to order (separated by spaces): ").split()))
                        restaurant.place_order(logged_user, selected_items)

                    # Implement other functionalities: Order History, Update Profile

                    elif user_choice == '4':
                        break

        elif choice == '3':
            break

if __name__ == "__main__":
    main()

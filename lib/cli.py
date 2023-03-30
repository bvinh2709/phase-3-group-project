#### IDEA: RESTAURANT AND **CARRIER(S)** AND SUPPLIER(S)
from db.models import Restaurant, Carrier, Supplier
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CLI:
    def __init__(self, user_input):
        self.suppliers = [supplier for supplier in session.query(Supplier)]
        self.carriers = [carrier for carrier in session.query(Carrier)]
        self.restaurants = [restaurant for restaurant in session.query(Restaurant)]
        self.name = user_input
        self.start()

    def start(self):
        print(' ')
        print(f'                    💥💥💥 Welcome To CDTV Corp., {self.name}! 💥💥💥')
        print(' ')

        exit = False
        while exit == False:
            choice = input('''
            Type "list" to see info of
            - restaurants🍔
            - carriers🚙
            - suppliers📝
            --------------------------
            Type "add" to add
            - restaurants🍔
            - carriers🚙
            - suppliers📝
            --------------------------
            Type "delete" to delete unwanted
            - restaurants🍔
            - carriers🚙
            - suppliers📝
            --------------------------
            Type "search" to find
            - restaurants🍔
            - carriers🚙
            - suppliers📝
            --------------------------
            Input:
            ''')
            print(' ')
            if choice.lower() == "list":
                    show_data(self)
            elif choice.lower() == "add":
                    add_data(self)
            elif choice.lower() == "delete":
                    delete_data(self)
            elif choice.lower() == "search":
                    search_data(self)

            print(' ')
            user_input = input("            Would you like to exit now? (Type Y/N): ")
            print(' ')
            if user_input == "Y" or user_input == 'y':
                exit = True

        printer(self.name)

def add_data(self):
    user_action = input("            Type C to add a carrier 🚙, S to add a supplier 📝 or R to add a restaurant 🍔: ")
    print(' ')

    if user_action == "S" or user_action == "s":
        name = input("            Type supplier name: ")
        location = input("            Type supplier location: ")
        item_list = input("            Type supplier item list: ")
        print(f'           🎉🎉 {name} added successfully!! 🎉🎉')
        supplier = Supplier(name = name, location = location, item_list = item_list)

        session.add(supplier)
        session.commit()

        self.suppliers.append(supplier)

    elif user_action == "R" or user_action == "r":
        name = input("            Type restaurant name: ")
        location = input("            Type restaurant location: ")
        cuisine = input("            Type of restaurant: ")
        restaurant = Restaurant(name = name, location=location, cuisine=cuisine)
        print(f'            🎉🎉 {name} added successfully!!🎉🎉')
        session.add(restaurant)
        session.commit()

        self.restaurants.append(restaurant)

    elif user_action == "C" or user_action == "c":
        print_suppliers(self.suppliers)
        print_restaurants(self.restaurants)
        print(' ')
        user_input = input("            Don't see your Supplier📝 or Restaurant🍔? (Type N/Y): ")
        print(' ')

        while user_input != "N" and user_input != "n":
            add_data(self)
            print(' ')
            print_suppliers(self.suppliers)
            print_restaurants(self.restaurants)
            print(' ')
            user_input = input("            Don't see your Supplier📝 or Restaurant🍔? (Type N/Y): ")
            print(' ')

        create_carrier(self)

def create_carrier(self):
    user_supplier = input("            Type the number🔢 of the supplier from the list above: ")
    user_restaurant = input("            Type the number🔢 of the restaurant from the list above: ")
    name = input("            What is the carrier's🚙 name?: " )
    fee = input("            How much 💸💸 did you pay for the shipment?: $" )
    phone = input("            Carrier's contact number 📱?: " )

    carrier = Carrier(
            name = name,
            fee = fee,
            phone = phone,
            supplier_id = self.suppliers[int(user_supplier) - 1].id,
            restaurant_id = self.restaurants[int(user_restaurant) - 1].id
    )

    session.add(carrier)
    session.commit()

    self.carriers.append(carrier)
    print(' ')
    print('            🎉🎉 Carrier added successfully!! 🎉🎉')

    print_carrier(carrier)

def delete_data(self):
    user_action = input("            Type C to delete a carrier🚙, S to delete a supplier📝 or R to delete a restaurant🍔: ")
    print(' ')

    if user_action == "S" or user_action == "s":
        print_suppliers(self.suppliers)
        print(' ')
        name = input("            Type Supplier Name: ")
        doomed_supplier = session.query(Supplier).filter(Supplier.name == name).first()
        print(f'            😞😞😞 {name} is sadly deleted!! 😞😞😞')
        session.delete(doomed_supplier)
        session.commit()

    elif user_action == "R" or user_action == "r":
        print_restaurants(self.restaurants)
        print(' ')
        name = input("            Type Restaurant Name: ")
        doomed_restaurant = session.query(Restaurant).filter(Restaurant.name == name).first()
        print(f'            😞😞😞 {name} is sadly deleted!! 😞😞😞')
        session.delete(doomed_restaurant)
        session.commit()

    elif user_action == "C" or user_action == "c":
        print_carriers(self.carriers)
        print(' ')
        name = input("            Type Carrier Name: ")
        doomed_carrier = session.query(Carrier).filter(Carrier.name == name).first()
        print(f'            😞😞😞 {name} is sadly deleted!! 😞😞😞')
        session.delete(doomed_carrier)
        session.commit()


def search_data(self):
    user_action = input("           Type S to search carriers🚙 by supplier📝 or R to search carriers🚙 by restaurant🍔: ")
    print(' ')
    if user_action == "S" or user_action == "s":
        print_suppliers(self.suppliers)
        user_pick = input("            Type the number🔢 of the supplier from the list above to see carriers of that supplier: ")
        print(' ')
        print_carriers(self.suppliers[int(user_pick) - 1].carriers)
    elif user_action == "R" or user_action == "r":
        print_restaurants(self.restaurants)
        user_pick = input("          Type the number🔢 of the restaurant from the list above to see carriers from that restaurant: ")
        print(' ')
        print_carriers(self.restaurants[int(user_pick) - 1].carriers)

def show_data(self):
    user_action = input("            Type C to list your carriers🚙, S to list suppliers📝 or R to list restaurants🍔: ")
    print(' ')
    if user_action == "S" or user_action == "s":
        print_suppliers(self.suppliers)
        user_next_action = input("            Type a supplier's📝 name: ")
        print(' ')
        for supplier in self.suppliers:
            if user_next_action == supplier.name:
                print(f'            Hey! Welcome to {supplier.name}!')
                print(' ----------------------------------------------- ')
                print(f'            You can find us at {supplier.location}!')
                print(' ----------------------------------------------- ')
                print(f'            Here is what we offer: {supplier.item_list}')

        # for supplier in self.suppliers:
        #     if user_next_action == supplier.name:
        #         print(f'            Hey! Welcome to {supplier.name}! What Brings You Here Today?')
        #         user_following_action = input("            Type L to see Location💸, I to see items🍲: ")
        #         print(' ')
        #         if user_following_action == "L" or "l":
        #             print(f'            You can find this supplier at {supplier.location}!')
        #             # user_following_action2 = input("            Would you like to know about what this supplier offer? Type Y/N or yes/no ")
        #             # if user_following_action2 == "Y" or "y" or "YES" or "Yes":
        #             #     print(f'            {supplier.name} has {supplier.item_list}')
        #         elif user_following_action == "I" or "i":
        #             print(f'            {supplier.name} has {supplier.item_list}')

    elif user_action == "R" or user_action == "r":
        print_restaurants(self.restaurants)
        user_next_action = input("            Type a restaurant's📝 name: ")
        print(' ')
        for restaurant in self.restaurants:
            if user_next_action == restaurant.name:
                print(f'            Hey! Welcome to {restaurant.name}!')
                print(' ----------------------------------------------- ')
                print(f'            You can find us at {restaurant.location}!')
                print(' ----------------------------------------------- ')
                print(f'            {restaurant.name} is a {restaurant.cuisine} restaurant')

    elif user_action == "C" or user_action == "c":
        print_carriers(self.carriers)
        

def print_suppliers(suppliers):
    print(' ')
    print('            📝📝📝Suppliers 📝📝📝')
    print(' ')

    for index, supplier in enumerate(suppliers):
        print(f'            {index + 1}. {supplier.name}')

    print(' ')

def print_restaurants(restaurants):
    print(' ')
    print('            🍔🍔🍔 Restaurants 🍔🍔🍔')
    print(' ')

    for index, restaurant in enumerate(restaurants):
        print(f'            {index + 1}. {restaurant.name}')

    print(' ')

def print_carriers(carriers):
    print(' ')
    print('            🚙🚙🚙 Carriers 🚙🚙🚙')
    print(' ')

    for index, carrier in enumerate(carriers):
        print_carrier(carrier)
    print(' ')

def print_carrier(carrier):
    print(' ')
    print(f'            Restaurant: {carrier.restaurant.name}')
    print(f'            Supplier:   {carrier.supplier.name}')
    print(f'            Name:       {carrier.name}')
    print(f'            Fee:        {carrier.fee}')
    print(f'            Phone:      {carrier.phone}')

def printer(user_input):
    print(' ')
    print(f'            Goodbye {user_input}!')


if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Hello there! Please Enter Your Name: ")
    CLI(user_input)


#### testing git ####
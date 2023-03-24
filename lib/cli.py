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
        print(f'***** Welcome To CDTV Corp., {self.name}! *****')
        print(' ')

        exit = False
        while exit == False:
            choice = input(f'Type "list" to see the restaurants, carriers or suppliers, type "add" to add a bottle, winery or grape, type "search" to find bottles by winery or grape: ')
            print(' ')
            if choice.lower() == "list":
                    show_data(self)
            elif choice.lower() == "add":
                    add_data(self)
            elif choice.lower() == "search":
                    search_data(self)
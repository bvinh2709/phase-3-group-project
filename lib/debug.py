from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Supplier, Restaurant, Carrier

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    breakpoint()

    import ipdb; ipdb.set_trace
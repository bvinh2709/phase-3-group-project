from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurants_library.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    delivered_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    carriers = relationship('Carrier', backref=backref('restaurant'))

    def __repr__(self):
        return f'Restaurant(id={self.id}, ' + \
            f'name={self.name})'

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    item_list = Column(String())

    carriers = relationship('Carrier', backref=backref('supplier'))

    def __repr__(self):
        return f'Supplier(id={self.id}, ' + \
            f'name={self.name}), ' + \
            f'location={self.location}), ' + \
            f'item_list={self.item_list}) '


class Carrier(Base):
    __tablename__ = 'carriers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    fee = Column(Integer())
    phone = Column(String())
    supplier_id = Column(Integer(), ForeignKey('suppliers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))

    def __repr__(self):
        return f'Carrier(id={self.id}, ' + \
            f'name={self.name}), ' + \
            f'fee={self.fee}), ' + \
            f'phone={self.phone}), ' + \
            f'supplier_id={self.supplier_id}) ' + \
            f'restaurant_id={self.restaurant_id}) '


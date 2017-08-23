#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


def db_create(session):
    # create an instance of the restaurant class
    my_first_restaurant = Restaurant(name="Pizza Palace")
    # add the restaurant to the "staging zone"
    session.add(my_first_restaurant)
    # make the changes persistant
    session.commit()

    # The following line tells us that something has been created
    #print(session.query(Restaurant).all())

    # Let's add a MenuItem to our new restaurant
    cheesepizza = MenuItem(name="Cheese Pizza",
                           description="""Made with all natural ingredients and
                           fresh mozzarella""",
                           course="Entree",
                           price="$8.99",
                           restaurant=my_first_restaurant)
    session.add(cheesepizza)
    session.commit()
    # The following line tells us that something has been created
    #print(session.query(MenuItem).all())


def db_read(session):
    # Querying the database can be done through the ".query(..)" method.
    # the ".first()" will give us an object that represents the first row in
    # that table.
    first_result = session.query(Restaurant).first()
    print(first_result.name)

    # ".all()" will give us a list of restaurant objects
    restaurants = session.query(Restaurant).all()
    for restaurant in restaurants:
        print(restaurant.name+"\n")

    # more query commands can be found here: 
    # http://docs.sqlalchemy.org/en/rel_0_9/orm/query.html


if __name__ == "__main__":
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()

    #db_create(session)
    db_read(session)

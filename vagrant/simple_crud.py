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
    # print(session.query(Restaurant).all())

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
    # print(session.query(MenuItem).all())


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


def print_veggie_burgers(session):
    veggie_burgers = session.query(MenuItem).filter_by(name="Veggie Burger")
    for veggie_burger in veggie_burgers:
        print(veggie_burger.id)
        print(veggie_burger.name)
        print(veggie_burger.price)
        print(veggie_burger.restaurant.name)
        print("\n")


def db_update(session):
    # In this example we want to update the price of the "Veggie Burger"
    # of the restaurant called "Urban Burger".
    # First we need to find the corresponding entry:
    print_veggie_burgers(session)
    # by looking at the output, we now know that we have to update the
    # entry with id=8.

    urban_veggie_burger = session.query(MenuItem).filter_by(id=8).one()
    print(urban_veggie_burger.price)
    # Let's finally update the price :)
    urban_veggie_burger.price = "$2.99"
    session.add(urban_veggie_burger)
    session.commit()

    print_veggie_burgers(session)


if __name__ == "__main__":
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()

    # db_create(session)
    # db_read(session)
    db_update(session)

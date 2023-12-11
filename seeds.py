from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create an SQLite database in memory
engine = create_engine('sqlite:///database.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Create random restaurants
for _ in range(4):
    restaurant = Restaurant(name=fake.company(), price=fake.random_int(1, 5))
    session.add(restaurant)
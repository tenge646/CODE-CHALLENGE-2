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

# Create random customers
for _ in range(10):
    customer = Customer(first_name=fake.first_name(), last_name=fake.last_name())
    session.add(customer)    

# Link customers and restaurants with random reviews
restaurants = session.query(Restaurant).all()
customers = session.query(Customer).all()

for _ in range(15):  # Create 15 random reviews
    restaurant = fake.random_element(restaurants)
    customer = fake.random_element(customers)
    review = Review(star_rating=fake.random_int(1, 5), restaurant=restaurant, customer=customer)
    session.add(review)

session.commit()

# Print reviews for each restaurant
for restaurant in restaurants:
    print(f"Reviews for {restaurant.name}:")
    for review in restaurant.reviews:
        print(f"Review for {restaurant.name} by {review.customer.first_name} {review.customer.last_name}: {review.star_rating} stars")

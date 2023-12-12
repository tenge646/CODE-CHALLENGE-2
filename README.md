# Restaurant Review System

This project is a restaurant review system implemented using SQLAlchemy in Python. It allows users to manage restaurants, customers, and their reviews within an SQLite database. The system defines models for `Restaurant`, `Customer`, and `Review` entities along with their respective relationships.

## Table of Contents

-   [Overview]
-   [Features]
-   [Setup and Installation]
-   [Usage]
-   [Project Structure]
-   [Contributing]
-   [License]

## Overview

The restaurant review system provides a platform to manage restaurant data, customer information, and reviews left by customers for various restaurants. It establishes relationships where a `Restaurant` can have multiple `Review`s, a `Customer` can leave multiple `Review`s, and each `Review` belongs to both a `Restaurant` and a `Customer`.

The system utilizes SQLAlchemy to define models and manage interactions with an SQLite database. Faker library is used for generating sample data to seed the database.

## Features

-   **CRUD Operations:** Create, Read, Update, and Delete operations for `Restaurant`, `Customer`, and `Review` entities.
-   **Relationship Handling:** Manages relationships between `Restaurant`, `Customer`, and `Review` entities.
-   **Data Seeding:** Seeds the database with sample data for testing purposes using Faker library.

## Setup and Installation

To set up the project, follow these steps:

1.  **Clone the Repository:**
  
    
    `git clone https://github.com/your-username/restaurant-review-system.git`


2.  **Install Dependencies:**
 
    `pip install -r requirements.txt` 
    
3.  **Database Setup:**
    
    -   Ensure you have SQLite installed.
    -   Run the migrations to create the database and tables:
        
        bashCopy code
        
        `python models.py` 
        
4.  **Seed the Database (Optional):** It will use random data:
    
 

## Usage
- Run `python3 seeds.py`
The project can be utilized for managing restaurant review data within an SQLite database. After setting up the project and database, you can perform operations such as creating new restaurants, customers, and reviews, fetching data, and managing relationships between entities.

You can explore the codebase, modify the models, or extend the functionalities as needed for your specific use case.

## Project Structure

The project structure is organized as follows:

-   **`models.py`:** Defines SQLAlchemy models for `Restaurant`, `Customer`, and `Review`.
-   **`seeds.py`:** Seeds the database with sample data using Faker library.
-
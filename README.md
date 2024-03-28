# Movie Data Engineering Project

This project aims to collect details of movies starting with the letters 'S' and 'H' from various websites and APIs, store them in a database, and provide query capabilities to retrieve relevant data.

## Overview

The project consists of two main components:

1. Data Collection:
   - Utilizes various web APIs to gather movie details.
   - Filters movies starting with the letters 'S' and 'H'.
   - Stores the filtered data in a database.

2. Database Schema and Query API:
   - Designs a database schema to store relevant movie details.
   - Provides query capabilities through Python scripts to extract meaningful insights from the database.

## Technologies Used

- Python for scripting and data manipulation.
- MySQL database for storing movie details.
- Requests library for making HTTP requests to APIs.
- Pandas library for data manipulation and filtering.
- SQLAlchemy library for database connection and data loading.

## Setup Instructions

1.Install dependencies:
   pip install mysql-connector-python
   pip install requests
   pip install pandas
   pip install sqlalchemy
2. Run MovieDetailAPI.py to collect movie data from APIs and store it in CSV files.
   Run Query.py to load filtered movie data into the MySQL database.

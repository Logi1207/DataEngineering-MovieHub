import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Logi@mysql",
  database="InviciblClouds"
)

# Create cursor
mycursor = mydb.cursor()

#1
# Query to retrieve the movies released in a year
query_choice = int(input("Enter the query number (1-7): "))
year = None
if query_choice == 1:
    year = int(input("Enter the year: "))
    query = """
        SELECT title, releaseDate
        FROM moviedetails
        WHERE YEAR(releaseDate) = %s
    """
    parameters = (year,)
    mycursor.execute(query, parameters)
    print("Movies released in the year", year)
    for row in mycursor.fetchall():
        print(row)

#2
# Query to retrieve a movie with respect to its starting letter
elif query_choice == 2:
    starting_letter = input("Enter the starting letter of the movie name: ").upper()
    query = """
        SELECT *
        FROM moviedetails
        WHERE startingLetter = %s
    """
    parameters = (starting_letter,)
    mycursor.execute(query, parameters)
    print("Movies starting with letter", starting_letter)
    for row in mycursor.fetchall():
        print(row)


#3
#Query to retrieve a top rated movies upto a range
elif query_choice == 3:
    top_n = int(input("Enter the number of top-rated movies you want to retrieve: "))
    query = """
        SELECT title , rating
        FROM moviedetails
        ORDER BY rating DESC
        LIMIT %s
    """
    parameters = (top_n,)
    mycursor.execute(query, parameters)
    print("Top", top_n, "rated movies:")
    for row in mycursor.fetchall():
        print(row)

#4
# Query to find a specific movie irrespective of case
elif query_choice == 4:
    movie_name = input("Enter the name of the movie you want to search for: ")
    query = """
        SELECT *
        FROM moviedetails
        WHERE LOWER(title) = LOWER(%s)
    """
    parameters = (movie_name,)
    mycursor.execute(query, parameters)
    found_movie = mycursor.fetchone()
    if found_movie:
        print("Movie found:")
        print(found_movie)
    else:
        print("Movie not found.")

#5
# Query to retrieve the most popular movie within a specific range of release dates
elif query_choice == 5:
    start_date = input("Enter the start date of the range (YYYY-MM-DD): ")
    end_date = input("Enter the end date of the range (YYYY-MM-DD): ")
    query = """
        SELECT movieId, title, overview, popularity, releaseDate,rating,voteCount
        FROM moviedetails
        WHERE releaseDate BETWEEN %s AND %s
        ORDER BY popularity DESC
        LIMIT 1
    """
    parameters = (start_date, end_date)
    mycursor.execute(query, parameters)
    most_popular_movie = mycursor.fetchone()
    if most_popular_movie:
        print("Most popular movie released between", start_date, "and", end_date)
        print(most_popular_movie)
    else:
        print("No movies found in the specified date range.")






# Close connection
mydb.close()

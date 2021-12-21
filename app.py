import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()

def prompt_new_movie():
    title = input("Insert movie title: ")
    release_timestamp = input("Insert movie release date (dd - mm - YYYY): ")
    parsed_date = datetime.datetime.strptime(release_timestamp, "%d-%m-%Y")
    database.add_movies(title, parsed_date.timestamp() )
    
    
def print_movie_list(heading, movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        print(f"{movie[0]} (on {movie_date})")
    print("----\n")

         
def prompt_whatch_movie():
    title = input("Which movie do you wanna see? ")
    database.watch_movie(title)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_new_movie()
    elif user_input == "2":
        heading = "Upcoming"
        movies = database.get_movies(heading)
        print_movie_list(heading, movies)        
    elif user_input == "3":
        heading = "All"
        movies = database.get_movies(heading)
        print_movie_list(heading, movies) 
    elif user_input == "4":
        prompt_whatch_movie()
    elif user_input == "5":
        heading = "whatched"
        movies = database.get_movies(heading)
        print_movie_list(heading, movies) 
    else:
        print("Invalid input, please try again!")
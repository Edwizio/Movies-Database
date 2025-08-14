from rapidfuzz import fuzz
import datetime
import movies_storage
import statistics
import random
import matplotlib.pyplot as plt
import sys

def list_movies():
    """
    This function returns a dictionary of dictionaries retrieved from the JSON database using the function defined
    in the movies storage file
    """

    movies = movies_storage.get_movies()

    total_movies = len(movies)
    print("\033[92mTotal movies: \033[0m", total_movies)

    for movie, info in movies.items():
        print(f"\033[92m{movie} : Rating : {info["Rating"]} and Year of Release : {info["Year"]}\033[0m")


def add_movie():
    """
    This function prompts user to enter a movie's name, checks if it already exists in the JSON Database
    and adds it there if it doesn't exist already, using the predefined functions in the movies_storage file.
    """

    # Getting the data from the JSON file
    movies = movies_storage.get_movies()

    movie = input("\033[95mEnter new movie name: \033[0m")
    found = False # flag to indicate found or not found status

    if movie.strip() == "":
        print("\033[91mPlease enter a valid name!\033[0m")

    for title in movies:
        if movie.lower() == title.lower():
            print(f"\033[92mMovie {movie} already exist!\033[0m")
            found = True
            break

    if not found:
        try:
            rating = float(input("\033[95mEnter movie rating: \033[0m"))
            year = int(input("\033[95mEnter the year of release: \033[0m"))
            # Adding in the JSON Database
            movies_storage.add_movie(movie, year, rating)

            print(f"\033[91mMovie {movie} successfully added.\033[0m")

        except ValueError:
            print(f"\033[91mPlease enter a numeric value\033[0m")


def remove_movie():
    """
    This function prompts user to enter a movie's name, checks if it already exists in the JSON Database
    and deletes it there if it exists there, using the predefined functions in the movies_storage file.
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()
    movie = input("\033[95mEnter movie name: \033[0m")

    found = False # flag to indicate found or not found status

    if movie.strip() == "":
        print("\033[91mPlease enter a valid name!\033[0m")

    for title in movies:
        if movie.lower() == title.lower():
            # Deleting the movie from the Database
            movies_storage.delete_movie(title)
            print(f"\033[92mMovie {title} successfully deleted.\033[0m")
            found = True

    if not found:
        print(f"\033[91mMovie {movie} doesn't exist!\033[0m")


def update_movies():
    """
    This function prompts user to enter a movie's name, checks if it already exists in the JSON Database
    and updates its rating using the predefined functions in the movies_storage file.
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()

    movie = input("\033[95mEnter movie name: \033[0m")
    found = False # flag to indicate found or not found status

    if movie.strip() == "":
        print("\033[91mPlease enter a valid name!\033[0m")

    for title in movies:
        if movie.lower() == title.lower():
            try:
                found = True
                rating = float(input("\033[95mEnter the new movie rating: \033[0m"))

                # Updating the rating in the JSON Database
                movies_storage.update_movie(title, rating)

                print(f"\033[92mMovie {title} updated.\033[0m")
                break

            except ValueError:
                print(f"\033[91mPlease enter a numeric value\033[0m")

    if not found:
        print(f"\033[91mMovie {movie} doesn't exist!\033[0m")


def stats():
    """
    This function prints some basic stats of the JSON Database like the average rating, the
    median rating, the highest rated movie and the lowest rated movie.
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()

    ratings = []
    # Storing the ratings of the movies in a list for further manipulation.
    for movie in movies.values():
        ratings.append(movie["Rating"])

    average_rating = statistics.mean(ratings)
    print(f"\033[92mAverage rating: {average_rating:.2f}\033[0m")

    median_rating = statistics.median(ratings)
    print(f"\033[94mMedian rating: {median_rating:.2f}\033[0m")

    max_rating = max(ratings)
    for key in movies:
        if movies[key]["Rating"] == max_rating:
            print(f"\033[96mBest Movie: {key}, {max_rating:.2f}\033[0m")

    min_rating = min(ratings)
    for key in movies:
        if movies[key]["Rating"] == min_rating:
            print(f"\033[91mWorst Movie: {key}, {min_rating:.2f}\033[0m")


def random_movie():
    """
    This function navigates through the JSON Database and returns a random movie as the choice
    of movie for tonight using the random module.
    """
    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()

    movies_list = list(movies.keys())
    movie = random.choice(movies_list)
    print(f"\033[92mYour movie for tonight: {movie},  it's rated {movies[movie]}\033[0m")


def search_movie():
    """
    This prompts the user to input part of a movies name and prints the movie or movies
    which have the user's entered data in their names from the JSON Database.
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()

    part_of_movie = input("\033[95mEnter part of movie name: \033[0m")
    is_found = False  # Flag to track if movie is found or not

    if part_of_movie.strip() == "":
        print("\033[91mPlease enter a valid name!\033[0m")

    else:
        for movie in movies.keys():
            if part_of_movie.lower() in movie.lower():
                print(f"\033[92m{movie}, {movies[movie]}\033[0m")
                is_found = True
                break

            elif fuzz.ratio(movie, part_of_movie) >= 50.0:
                print(f"\033[93mThe movie {part_of_movie} does not exist. Did you mean: {movie} ?\033[0m")
                is_found = True
                break

    if not is_found:
        print("\033[91mMovie not found!\033[0m")


def movies_sorted():
    """
    This function sorts the JSON Database on the basis of the rating of the movies going
    from highest to the lowest.
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()

    # Prompting user to give the relevant choice.
    choice = input("\033[95mPlease enter to R or Y, if you want the sort based on rating or year: \033[0m")

    if choice == "R" or choice == "r":
        sorted_by_rating = sorted(movies.items(), key=lambda item: item[1]["Rating"], reverse=True)
        for movie, rating in sorted_by_rating:
            print(f"\033[92m{movie} : {rating["Rating"]}\033[0m")

    elif choice == "Y" or choice == "y":
        order = input("\033[95mPlease enter L of O if you want the latest or oldest movie on the top: \033[0m")

        if order == "L" or order == "l":
            sorted_by_latest_year = sorted(movies.items(), key=lambda item: item[1]["Year"], reverse=True)
            for movie, year in sorted_by_latest_year:
                print(f"\033[92m{movie} : {year["Year"]}\033[0m")

        elif order == "O" or order == "o":
            sorted_by_oldest_year = sorted(movies.items(), key=lambda item: item[1]["Year"])
            for movie, year in sorted_by_oldest_year:
                print(f"\033[92m{movie} : {year["Year"]}\033[0m")

        else:
            print("\033[92mPlease enter a valid option.\033[0m")

    else:
        print("\033[92mPlease enter a valid option.\033[0m")


def filter_movies():
    """
    The function should prompt the user to input the minimum rating, start year, and end year.
If the user leaves any input blank, it should be considered as no minimum rating, start year, or end year, respectively.
It should filter the list of movies based on the provided criteria.
The filtered movies should be displayed with their titles, release years, and ratings.
    :return:
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()


    minimum_rating = input("\033[95mEnter minimum rating (leave blank for no minimum rating): \033[0m")
    if minimum_rating.strip() == "":
        # Setting the default value of minimum rating to the average rating
        minimum_rating = statistics.mean(movie["Rating"] for movie in movies.values())

    start_year = input("\033[95mEnter start year (leave blank for no start year): \033[0m")

    end_year = input("\033[95mEnter end year (leave blank for no end year): \033[0m")

    if end_year.strip() == "":
        # Setting the default value of end_year to the current year
        current_date = datetime.datetime.now()
        end_year = current_date.year

    if start_year.strip() == "":
        # Setting the default value of minimum_year to the current year
        start_year = end_year - 20

    filtered_movies = [movie for movie, info in movies.items() if info["Rating"] > float(minimum_rating) and
                       int(start_year) <= info["Year"] <= int(end_year)]
    if not filtered_movies:
        print("\033[92mSorry! No movie matches the entered criteria.\033[0m")

    else:
        print("\033[92mFiltered Movies: \033[0m")

        for movie, info in movies.items():
            if movie in filtered_movies:
                print(f"\033[92m{movie} ({info["Year"]}): {info["Rating"]}\033[0m")


def rating_histogram():
    """
    This functions plots a histogram based on the movies rating.
    """

    # Loading the Database using the movies_storage file
    movies = movies_storage.get_movies()

    ratings = []
    # Storing the ratings of the movies in a list for further manipulation.
    for movie in movies.values():
        ratings.append(movie["Rating"])

    plt.hist(ratings, color = 'green')
    plt.xlabel("Movie Ratings")
    plt.ylabel("Movies Names")
    plt.title("Histogram of Ratings")
    plt.show()
    plt.savefig(r"C:\Users\ilhan\Pictures\plot_histogram.jpeg") # Saves the histogram in this file


def exit_menu():
    """
    This function exits program from command line interface (CLI) using the sys module.
    """
    print("\033[92mBye\033[0m")
    sys.exit(0)


def print_menu():
    """
    This function prints the command line interface (CLI) menu of the program.
    """
    print("\033[94m** ** ** ** ** My Movies Database ** ** ** ** **\033[0m")

    print("\033[94mMenu: \033[0m")
    print("\033[94m0. Exit")
    print("\033[94m1. List movies\033[0m")
    print("\033[94m2. Add movie\033[0m")
    print("\033[94m3. Delete movie\033[0m")
    print("\033[94m4. Update movie\033[0m")
    print("\033[94m5. Stats\033[0m")
    print("\033[94m6. Random movie\033[0m")
    print("\033[94m7. Search movie\033[0m")
    print("\033[94m8. Movies sorted by rating or year\033[0m")
    print("\033[94m9. Create Rating Histogram\033[0m")
    print("\033[94m10. Filtered movies\033[0m")


def user_input():
    """
    This function directs the program flow to the correct function based on the user input.
    """
    try:
        user_choice = int(input("\033[95mEnter choice (0-9): "))

        if user_choice == 0:
            exit_menu()
        elif user_choice == 1:
            list_movies()
        elif user_choice == 2:
            add_movie()
        elif user_choice == 3:
            remove_movie()
        elif user_choice == 4:
            update_movies()
        elif user_choice == 5:
            stats()
        elif user_choice == 6:
            random_movie()
        elif user_choice == 7:
            search_movie()
        elif user_choice == 8:
            movies_sorted()
        elif user_choice == 9:
            rating_histogram()
        elif user_choice == 10:
            filter_movies()
        else:
            print("\033[91mOption not available. Please enter a number from 0-9.\033[0m")

    except ValueError:
        print("\033[91mInvalid input. Please enter a numeric value.\033[0m")


def main():
    """
    This is the main function where the nested structure is stored and all the functions are being implemented.
    """

    # An infinite loop to ensure the always prompting logic of command line interface (CLI).
    while True:
        print_menu()
        user_input()


if __name__ == "__main__":
    main()

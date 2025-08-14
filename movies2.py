import movies_storage
import statistics
import random
import matplotlib.pyplot as plt
import sys

def list_movies(movies):
    """
    This function receives a dictionary of dictionaries as input and prints out the contents.
    :param (dictionary of dictionaries) movies:
    """

    total_movies = len(movies)
    print("Total movies: ", total_movies)

    for movie, info in movies.items():
        print(f"{movie} : Rating : {info["Rating"]} and Year of Release : {info["Year"]}")


def add_movie(movies):
    """
    This function prompts a user to enter a movie, it's rating and the year of release, adds the information
    subsequently to the nested dictionary movies and prints out the successful addition message.
    :param (dictionary of dictionaries) movies:
    """

    movie = input("Enter movie name: ")
    rating = float(input("Enter movie rating: "))
    year = int(input("Enter the year of release: "))
    movies[movie] = { "Rating": rating, "Year": year }
    print(f"Movie {movie} successfully added.")


def remove_movie(movies):
    """
    This function prompts  the user to input the name of the movie to be deleted from the nested structure,
    checks if the movie exists or not, deletes the movie if found and displays the relevant message.
    :param (dictionary of dictionaries) movies:
    """

    movie = input("Enter movie name: ")
    if movie in movies:
        del movies[movie]
        print(f"Movie {movie} successfully deleted.")
    else:
        print(f"Movie {movie} doesn't exist!")


def update_movies(movies):
    """
    This function updates the rating of a movie in the nested structure if it exists inside it.
    :param (dictionary of dictionaries) movies:
    """

    movie = input("Enter movie name: ")
    if movie not in movies:
        print(f"Movie {movie} doesn't exist!")

    else:
        rating = float(input("Enter new movie rating: "))
        movies[movie]["Rating"] = rating
        print(f"Movie {movie} updated.")


def stats(movies):
    """
    This function prints some basic stats of the nested structure like the average rating, the
    median rating, the highest rated movie and the lowest rated movie.
    :param (dictionary of dictionaries) movies:
    """

    ratings = []
    # Storing the ratings of the movies in a list for further manipulation.
    for movie in movies.values():
        ratings.append(movie["Rating"])

    average_rating = statistics.mean(ratings)
    print(f"Average rating: {average_rating}")

    median_rating = statistics.median(ratings)
    print(f"Median rating: {median_rating}")

    max_rating = max(ratings)
    for key in movies:
        if movies[key]["Rating"] == max_rating:
            print(f"Best Movie: {key}, {max_rating}")

    min_rating = min(ratings)
    for key in movies:
        if movies[key]["Rating"] == min_rating:
            print(f"Worst Movie: {key}, {min_rating}")


def random_movie(movies):
    """
    This function takes the nested structure as argument and returns a random movie as the choice
    of movie for tonight using the random module.
    :param (dictionary of dictionaries) movies:
    """

    movies_list = list(movies.keys())
    movie = random.choice(movies_list)
    print(f"Your movie for tonight: {movie},  it's rated {movies[movie]}")


def search_movie(movies):
    """
    This prompts the user to input part of a movies name and prints the movie or movies
    which have the user's entered data in their names.
    :param (dictionary of dictionaries) movies:
    """

    part_of_movie = input("Enter part of movie name: ")
    for movie in movies.keys():
        if part_of_movie.lower() in movie.lower():
            print(f"{movie}, {movies[movie]}")


def movies_sorted(movies):
    """
    This function sorts the nested structure on the basis of the rating of the movies going
    from highest to the lowest.
    :param (dictionary of dictionaries) movies:
    """

    sorted_by_rating = dict(sorted(movies.items(), key=lambda item: item[1]["Rating"], reverse=True))
    for movie, rating in sorted_by_rating.items():
        print(f"{movie} : {rating}")


def rating_histogram(movies):
    """
    This functions plots a histogram based on the movies rating.
    :param (dictionary of dictionaries) movies:
    """

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
    print("Bye")
    sys.exit(0)


def print_menu():
    """
    This function prints the command line interface (CLI) menu of the program.
    """
    print("** ** ** ** ** My Movies Database ** ** ** ** **")

    print("Menu: ")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Create Rating Histogram")


def user_input(movies):
    """
    This function directs the program flow to the correct function based on the user input.
    :param (dictionary of dictionaries) movies:
    """
    user_choice = int(input("Enter choice (0-9): "))

    if user_choice == 0:
        exit_menu()
    elif user_choice == 1:
        list_movies(movies)
    elif user_choice == 2:
        add_movie(movies)
    elif user_choice == 3:
        remove_movie(movies)
    elif user_choice == 4:
        update_movies(movies)
    elif user_choice == 5:
        stats(movies)
    elif user_choice == 6:
        random_movie(movies)
    elif user_choice == 7:
        search_movie(movies)
    elif user_choice == 8:
        movies_sorted(movies)
    elif user_choice == 9:
        rating_histogram(movies)
    else:
        print("Invalid input. Please try again.")


def main():
    """
    This is the main function where the nested structure is stored and all the functions are being implemented.
    """

    # Dictionary of dictionaries to store the movies and their rating with the year of release.
    movies = {
        "The Shawshank Redemption": { "Rating" : 9.5, "Year" : 1994 },
        "Pulp Fiction": { "Rating" : 8.8, "Year" : 1994 },
        "The Room": { "Rating" : 3.6, "Year" : 2003 },
        "The Godfather": { "Rating" : 9.2, "Year" : 1972 },
        "The Godfather: Part II": { "Rating" : 9.0, "Year" : 1974 },
        "The Dark Knight": { "Rating" : 9.0, "Year" : 2008 },
        "12 Angry Men": { "Rating" : 8.9, "Year" : 1957 },
        "Everything Everywhere All At Once": { "Rating" : 8.9, "Year" : 2022 },
        "Forrest Gump": { "Rating" : 8.8, "Year" : 1994 },
        "Star Wars: Episode V": { "Rating" : 8.7, "Year" : 1980 }
    }

    # An infinite loop to ensure the always prompting logic of command line interface (CLI).
    while True:
        print_menu()
        user_input(movies)


if __name__ == "__main__":
    main()

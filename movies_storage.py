import json

def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    with open("data.json", "r") as reader:
        data = json.loads(reader.read())

    return data


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    json_str = json.dumps(movies)

    with open("data.json", "w") as writer:
        writer.write(json_str)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies' database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data.json", "r") as reader:
        data = json.loads(reader.read())
        data[title] = {"Year": year, "Rating" : rating}
        json_str = json.dumps(data)

    with open("data.json", "w") as writer:
        writer.write(json_str)


def delete_movie(title):
    """
    Deletes a movie from the movies' database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data.json", "r") as reader:
        data = json.loads(reader.read())
        del data[title]

        json_str = json.dumps(data)

    with open("data.json", "w") as writer:
        writer.write(json_str)


def update_movie(title, rating):
    """
    Updates a movie from the movies' database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data.json", "r") as reader:
        data = json.loads(reader.read())
        data[title]["Rating"] = rating

        json_str = json.dumps(data)

    with open("data.json", "w") as writer:
        writer.write(json_str)




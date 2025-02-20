# Initialize a List of Movies
movie_collection = [
    ("The Shawshank Redemption", "Frank Darabont", 1994),
    ("The Godfather", "Francis Ford Coppola", 1972),
    ("The Dark Knight", "Christopher Nolan", 2008),
    ("Pulp Fiction", "Quentin Tarantino", 1994),
    ("Forrest Gump", "Robert Zemeckis", 1994),
    ("Inception", "Christopher Nolan", 2010),
    ("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999),
    ("Fight Club", "David Fincher", 1999)
]

def display_movies():
    print("Movie Collection")
    for title,director,year in movie_collection:
        print(f"Title:{title}, Director {director}, Year {year}")

display_movies()

def add_movie(title, director, year):
    new_movie=(title,director,year)
    movie_collection.append(new_movie)
    print(f"Movie {title} by director {director} added to collection")

add_movie("The Empire Strikes Back","Irvin Kershner", 1980)

display_movies()

def search_by_director(director):
    movies_by_director=[]
    for movie in movie_collection:
        title,movie_director,year=movie
        if director.lower()==movie_director.lower():
            movies_by_director.append(movie)
    return movies_by_director

add_movie("Se7en", "David Fincher", 1995)

movies_by_Fincher= search_by_director("David Fincher")
print("Movies by David Fincher")
for title,director, year in movies_by_Fincher:
    print(f"Title: {title}, Year:{year}")

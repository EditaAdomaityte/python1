favorite_movies=[]

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.")

def display_movies():
    print("Favorite Movies:")
    for movie in favorite_movies:
        print(f"-{movie}")

#Count Movies in the List
def count_movies():
    return len(favorite_movies)

#or to count movies
def counting_movies():
    count=0
    for _ in favorite_movies:
        count+=1
    return count

#or
def counting_movie():
    return sum(1 for _ in favorite_movies)

#find the movie
def find_movie(movie):
    if movie in favorite_movies:
        print(f"Movie '{movie}' is in Favorite Movies list")
    else:
       print(f"Movie '{movie}' is not in Favorite Movies list") 

#deleting all movies from a list
def delete_all_movies():
    favorite_movies.clear()
    print("The List has been cleared")

#Adding movies
add_movie("Titanic")
add_movie("101 Dalmatians")
add_movie("Gladiator")
add_movie("The Count of Monte Cristo")

display_movies()

count_movies()

remove_movie("Titani")
remove_movie("Titanic")

display_movies()

find_movie("Titanic")

find_movie("Gladiator")

print(f"Total movies using len: {count_movies()}")  # Prints the result of count_movies()
print(f"Total movies using manual counting: {counting_movies()}")  # Prints the result of counting_movies()
print(f"Total movies using sum: {counting_movie()}")  # Prints the result of counting_movie()

delete_all_movies()

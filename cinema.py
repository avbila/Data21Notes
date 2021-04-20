# Creating a dictionary for the films in the cinema:
movie_details = {
    "The Shawshank Redemption": {"Age Rating": "15+"},
    "The Godfather": {"Age Rating": "15+"},
    "Fight Club" : {"Age Rating": "18+"},
    "The Lord of the Ring":{"Age Rating": "PG"},
    "Pulp Fiction" : {"Age Rating": "15+"},
    "Forest Gump": {"Age Rating": "PG"},
    "Inception" : {"Age Rating": "PG"},
    "Finding Nemo" : {"Age Rating": "U"},
    "The Silence of the Lambs": {"Age Rating": "18+"},
    "Saving Private Ryan":{"Age Rating": "15+"}
}

#Asking user to enter their name:
name = input('Please Enter Your Name: \n')

#Asking user to enter their age:
while True:
    age = input("Please Enter Your Age:  \n")
    if age.isdigit() and int(age)>0 and int(age)<=120:
        age = int(age)
        break
    else:
        print("Incorrect entry !")
        print("Please try again.")

#Determining the list of allowed film ratings:
if age < 12:
    ratings_allowed = ["U"]
elif age < 15 :
    ratings_allowed = ["U","PG"]
elif age < 18:
    ratings_allowed = ["U","PG","15+"]
else:
    ratings_allowed = ["U", "PG", "15+","18+"]

#Getting a list of movie allowed to see:
allowed_movies =[]
for movie in movie_details.keys():
    if movie_details[movie]['Age Rating'] in ratings_allowed:
        allowed_movies.append(movie)

#Displaying the results to the user:
print(f"Hello {name}")
print("The movies available to see are:\n")
for movie in allowed_movies:
    print(movie)
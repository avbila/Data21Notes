# Creating a dictionary for the films in the cinema:
movie_details = {
    "The Shawshank Redemption": {"Age Rating": "15+"},
    "The Godfather": {"Age Rating": "15+"},
    "Fight Club": {"Age Rating": "18+"},
    "The Lord of the Ring": {"Age Rating": "PG"},
    "Pulp Fiction": {"Age Rating": "15+"},
    "Forest Gump": {"Age Rating": "PG"},
    "Inception": {"Age Rating": "PG"},
    "Finding Nemo": {"Age Rating": "U"},
    "The Silence of the Lambs": {"Age Rating": "18+"},
    "Saving Private Ryan": {"Age Rating": "15+"}
}

# Asking user to enter their name:
while True:
    name = input('Please Enter Your Name: \n')
    if name.isalpha():
        break
    else:
        print("Incorrect entry !\nPlease Enter Your First Name only.")


# Asking user to enter their age:
while True:
    age = input("Please Enter Your Age:  \n")
    if age.isdigit() and 0 < int(age) <= 120:
        age = int(age)
        break
    else:
        print("Incorrect entry !\nPlease try again.")

# Determining the list of allowed film ratings:
if age < 12:
    ratings_allowed = ["U"]
elif age < 15:
    ratings_allowed = ["U", "PG"]
elif age < 18:
    ratings_allowed = ["U", "PG", "15+"]
else:
    ratings_allowed = ["U", "PG", "15+", "18+"]

# Getting a list of movie allowed to see:
allowed_movies = []
for movie in movie_details.keys():
    if movie_details[movie]['Age Rating'] in ratings_allowed:
        allowed_movies.append(movie)

# Displaying the results to the user:
print(f"\nHello {name}\nThe movies available to see are:\n")
for movie in allowed_movies:
    print(movie)


# def check_movies():
#     E0.delete(0, END)
#     age =int(E2.get())
#     name=str(E1.get())
#     # Creating a dictionary for the films in the cinema:
#     movie_details = {
#         "The Shawshank Redemption": {"Age Rating": "15+"},
#         "The Godfather": {"Age Rating": "15+"},
#         "Fight Club": {"Age Rating": "18+"},
#         "The Lord of the Ring": {"Age Rating": "PG"},
#         "Pulp Fiction": {"Age Rating": "15+"},
#         "Forest Gump": {"Age Rating": "PG"},
#         "Inception": {"Age Rating": "PG"},
#         "Finding Nemo": {"Age Rating": "U"},
#         "The Silence of the Lambs": {"Age Rating": "18+"},
#         "Saving Private Ryan": {"Age Rating": "15+"}
#     }
#
#     # Determining the list of allowed film ratings:
#     if age < 12:
#         ratings_allowed = ["U"]
#     elif age < 15:
#         ratings_allowed = ["U", "PG"]
#     elif age < 18:
#         ratings_allowed = ["U", "PG", "15+"]
#     else:
#         ratings_allowed = ["U", "PG", "15+", "18+"]
#
#     # Getting a list of movie allowed to see:
#     allowed_movies = []
#     for movie in movie_details.keys():
#         if movie_details[movie]['Age Rating'] in ratings_allowed:
#             allowed_movies.append(movie)
#
#     # Displaying the results to the user:
#     print(f"Hello {name}")
#     print("The movies available to see are:\n")
#     for movie in allowed_movies:
#         print(movie)
#     E0.insert(INSERT,allowed_movies)
#     return
#
#
#
#
#
#
#
# #Designing the GUI:
# from tkinter  import *
# master = Tk()
#
# #Creat a frame to put a grid of labels and buttons:
# topFrame = Frame(master, bg = "black", width = 2500, height= 100)
# topFrame.pack(fill=BOTH,expand=1)
#
# L1=Label(topFrame, text = "Please Enter Your details:",bg="white")
# L2=Label(topFrame, text = "Name:",bg="white")
# L3=Label(topFrame, text = "Age:",bg="white")
# E0=Entry(topFrame,bg="white")
# E1=Entry(topFrame,bg="white")
# E2=Entry(topFrame,bg="white")
# B1=Button(topFrame,text="Check Available movies",command=check_movies)
#
# L1.grid(column=0, row=0, sticky=W+E+N+S, padx=5, pady=5, columnspan=2)
# L2.grid(column=0, row=1, sticky=W+E+N+S, padx=5, pady=5)
# E1.grid(column=1, row=1, sticky=W+E+N+S, padx=5, pady=5)
# L3.grid(column=0, row=2, sticky=W+E+N+S, padx=5, pady=5)
# E2.grid(column=1, row=2, sticky=W+E+N+S, padx=5, pady=5)
# B1.grid(column=0, row=3, sticky=W+E+N+S, padx=5, pady=5, columnspan=2)
# E0.grid(column=0, row=4, sticky=W+E+N+S, padx=5, pady=5, columnspan=2)
#
# master.mainloop()


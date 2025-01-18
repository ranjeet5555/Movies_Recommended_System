
## YAh sabse sahi se
import streamlit as st
import pickle
import pandas as pd
import requests

# Theme toggler
theme = st.radio("Choose Theme:", ["Light", "Dark"], horizontal=True)

# Dynamic CSS for dark mode
if theme == "Dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117; /* Dark background */
            color: #00ff00; /* General text color for dark mode */
        }
        .stApp {
            background-color: #0e1117;
        }
        /* Change dropdown headings color to light green in dark mode */
        div[data-testid="stSelectbox"] label {
            color: #90ee90 !important; /* Light green for labels */
            font-weight: bold; /* Optional: Make the font bold */
        }
        /* Change the main title color to light green in dark mode */
        h1 {
            color: #90ee90 !important; /* Light green for title */
        }
        .stButton > button {
            background-color: #00ff00; /* Green button background */
            color: black;
            font-weight: bold;
            border: none;
        }
        .stButton > button:hover {
            background-color: #32cd32; /* Lighter green on hover */
        }
        /* Style recommended movie names */
        .recommended-movie-name {
            color: #00ff00; /* Green color for movie names in dark mode */
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff; /* Light mode background */
            color: #000000; /* Default text color for light mode */
        }
        .stApp {
            background-color: #ffffff;
        }
        .stButton > button {
            background-color: #1e90ff; /* Blue button background */
            color: white;
        }
        .stButton > button:hover {
            background-color: #4682b4; /* Darker blue on hover */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to fetch the poster of the movie using its ID
def fetchPoster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Available"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"

# Function to recommend movies based on similarity
def Recommended(movie, similarity_distance=None):
    if similarity_distance is None:
        st.error("The similarity distance matrix is not loaded.")
        return [], []

    if movie not in movies['title'].values:
        st.error("The selected movie is not in the dataset.")
        return [], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_distance[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    Recommende_movies = []
    Recommende_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
        Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
        Recommende_movies_poster.append(fetchPoster(movie_id))  # Append movie poster
    return Recommende_movies, Recommende_movies_poster

# Load the movie dictionary
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load the similarity matrix
similarity_distance = pickle.load(open('similarity_distance.pkl', 'rb'))

# Title of the Streamlit app
st.title('🎬 Movie Recommendation System')

# Dropdown for selecting a movie
selected_movie_name = st.selectbox("Choose a Movie to Get Recommendations:", movies['title'].values)

# Dropdown for selecting the number of movies per row
movies_per_row = st.selectbox(
    "Choose Number of Movies Per Row:",
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Options for user to choose from
    index=4  # Default to 5 movies per row
)

# Button to recommend movies
if st.button('Recommend'):
    names, posters = Recommended(selected_movie_name, similarity_distance)

    # Display movies in rows based on user-selected filter
    for i in range(0, len(names), movies_per_row):  # Iterate in chunks of user-selected size
        cols = st.columns(movies_per_row)  # Create the specified number of columns
        for col, name, poster in zip(cols, names[i:i+movies_per_row], posters[i:i+movies_per_row]):
            with col:
                st.image(poster, use_container_width=True)  # Display poster
                # Add recommended movie names styled with CSS
                st.markdown(f"<p class='recommended-movie-name'>{name}</p>", unsafe_allow_html=True)



## YAh bhi sahi h lekin isme slide bar wala code hai
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Dark/Light mode toggle with icons 🌞 and 🌙
# if "theme" not in st.session_state:
#     st.session_state["theme"] = "Light"  # Default to Light mode
#
# # Toggle button for theme
# toggle_theme = st.sidebar.button("🌞" if st.session_state["theme"] == "Light" else "🌙")
#
# if toggle_theme:
#     st.session_state["theme"] = "Dark" if st.session_state["theme"] == "Light" else "Light"
#
# # Dynamic CSS based on the theme
# if st.session_state["theme"] == "Dark":
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #0e1117; /* Dark background */
#             color: #00ff00; /* General text color for dark mode */
#         }
#         .stApp {
#             background-color: #0e1117;
#         }
#         /* Change dropdown headings color to light green in dark mode */
#         div[data-testid="stSelectbox"] label {
#             color: #90ee90 !important; /* Light green for labels */
#             font-weight: bold; /* Optional: Make the font bold */
#         }
#         /* Change the main title color to light green in dark mode */
#         h1 {
#             color: #90ee90 !important; /* Light green for title */
#         }
#         .stButton > button {
#             background-color: #00ff00; /* Green button background */
#             color: black;
#             font-weight: bold;
#             border: none;
#         }
#         .stButton > button:hover {
#             background-color: #32cd32; /* Lighter green on hover */
#         }
#         /* Style recommended movie names */
#         .recommended-movie-name {
#             color: #00ff00; /* Green color for movie names in dark mode */
#             font-weight: bold;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
# else:
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #ffffff; /* Light mode background */
#             color: #000000; /* Default text color for light mode */
#         }
#         .stApp {
#             background-color: #ffffff;
#         }
#         .stButton > button {
#             background-color: #1e90ff; /* Blue button background */
#             color: white;
#         }
#         .stButton > button:hover {
#             background-color: #4682b4; /* Darker blue on hover */
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             return "https://via.placeholder.com/500x750?text=No+Image+Available"
#     except requests.exceptions.RequestException:
#         return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"
#
# # Function to recommend movies based on similarity
# def Recommended(movie, similarity_distance=None):
#     if similarity_distance is None:
#         st.error("The similarity distance matrix is not loaded.")
#         return [], []
#
#     if movie not in movies['title'].values:
#         st.error("The selected movie is not in the dataset.")
#         return [], []
#
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity_distance[movie_index]
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
#
#     Recommende_movies = []
#     Recommende_movies_poster = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movie_id))  # Append movie poster
#     return Recommende_movies, Recommende_movies_poster
#
# # Load the movie dictionary
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # Load the similarity matrix
# similarity_distance = pickle.load(open('similarity_distance.pkl', 'rb'))
#
# # Title of the Streamlit app
# st.title('🎬 Movie Recommendation System')
#
# # Dropdown for selecting a movie
# selected_movie_name = st.selectbox("Choose a Movie to Get Recommendations:", movies['title'].values)
#
# # Dropdown for selecting the number of movies per row
# movies_per_row = st.selectbox(
#     "Choose Number of Movies Per Row:",
#     options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Options for user to choose from
#     index=4  # Default to 5 movies per row
# )
#
# # Button to recommend movies
# if st.button('Recommend'):
#     names, posters = Recommended(selected_movie_name, similarity_distance)
#
#     # Display movies in rows based on user-selected filter
#     for i in range(0, len(names), movies_per_row):  # Iterate in chunks of user-selected size
#         cols = st.columns(movies_per_row)  # Create the specified number of columns
#         for col, name, poster in zip(cols, names[i:i+movies_per_row], posters[i:i+movies_per_row]):
#             with col:
#                 st.image(poster, use_container_width=True)  # Display poster
#                 # Add recommended movie names styled with CSS
#                 st.markdown(f"<p class='recommended-movie-name'>{name}</p>", unsafe_allow_html=True)


## Yah wala sahi h dark mode and light mode k liye
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Initialize session state for theme
# if "theme" not in st.session_state:
#     st.session_state["theme"] = "Light"  # Default to Light mode
#
# # Toggle theme function
# def toggle_theme():
#     if st.session_state["theme"] == "Light":
#         st.session_state["theme"] = "Dark"
#     else:
#         st.session_state["theme"] = "Light"
#
# # Toggle button for dark/light mode with emoji
# toggle_button = st.button(
#     f"{'🌙 Dark Mode' if st.session_state['theme'] == 'Light' else '🔆 Light Mode'}"
# )
#
# if toggle_button:
#     toggle_theme()
#
# # Apply dynamic CSS based on the theme
# if st.session_state["theme"] == "Dark":
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #0e1117;
#             color: #90ee90;
#         }
#         .stApp {
#             background-color: #0e1117;
#         }
#         div[data-testid="stSelectbox"] label {
#             color: #90ee90 !important;
#             font-weight: bold;
#         }
#         h1 {
#             color: #90ee90 !important;
#         }
#         .stButton > button {
#             background-color: #32cd32;
#             color: black;
#             font-weight: bold;
#             border: none;
#         }
#         .stButton > button:hover {
#             background-color: #00ff00;
#         }
#         .recommended-movie-name {
#             color: #00ff00;
#             font-weight: bold;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
# else:
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #ffffff;
#             color: #000000;
#         }
#         .stApp {
#             background-color: #ffffff;
#         }
#         div[data-testid="stSelectbox"] label {
#             color: #000000 !important;
#             font-weight: bold;
#         }
#         h1 {
#             color: #000000 !important;
#         }
#         .stButton > button {
#             background-color: #1e90ff;
#             color: white;
#             font-weight: bold;
#         }
#         .stButton > button:hover {
#             background-color: #4682b4;
#         }
#         .recommended-movie-name {
#             color: #1e90ff;
#             font-weight: bold;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             return "https://via.placeholder.com/500x750?text=No+Image+Available"
#     except requests.exceptions.RequestException:
#         return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"
#
# # Function to recommend movies based on similarity
# def Recommended(movie, similarity_distance=None):
#     if similarity_distance is None:
#         st.error("The similarity distance matrix is not loaded.")
#         return [], []
#
#     if movie not in movies['title'].values:
#         st.error("The selected movie is not in the dataset.")
#         return [], []
#
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity_distance[movie_index]
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
#
#     Recommende_movies = []
#     Recommende_movies_poster = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movie_id))  # Append movie poster
#     return Recommende_movies, Recommende_movies_poster
#
# # Load the movie dictionary
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # Load the similarity matrix
# similarity_distance = pickle.load(open('similarity_distance.pkl', 'rb'))
#
# # Title of the Streamlit app
# st.title('🎬 Movie Recommendation System')
#
# # Dropdown for selecting a movie
# selected_movie_name = st.selectbox("Choose a Movie to Get Recommendations:", movies['title'].values)
#
# # Dropdown for selecting the number of movies per row
# movies_per_row = st.selectbox(
#     "Choose Number of Movies Per Row:",
#     options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Options for user to choose from
#     index=4  # Default to 5 movies per row
# )
#
# # Button to recommend movies
# if st.button('Recommend'):
#     names, posters = Recommended(selected_movie_name, similarity_distance)
#
#     # Display movies in rows based on user-selected filter
#     for i in range(0, len(names), movies_per_row):  # Iterate in chunks of user-selected size
#         cols = st.columns(movies_per_row)  # Create the specified number of columns
#         for col, name, poster in zip(cols, names[i:i+movies_per_row], posters[i:i+movies_per_row]):
#             with col:
#                 st.image(poster, use_container_width=True)  # Display poster
#                 st.markdown(f"<p class='recommended-movie-name'>{name}</p>", unsafe_allow_html=True)

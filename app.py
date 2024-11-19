# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movies_id):
#     url = f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()
#
#         # Check if 'poster_path' exists in the response
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Return a placeholder image if 'poster_path' is not available
#             return "https://via.placeholder.com/500x750?text=No+Image"
#     except requests.exceptions.RequestException as e:
#         # Handle any errors in the API request gracefully
#         st.error(f"Error fetching poster: {e}")
#         return "https://via.placeholder.com/500x750?text=No+Image"
#
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
#         movies_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movies_id))  # Append movie poster
#     return Recommende_movies, Recommende_movies_poster
#
#
# # Load the movie dictionary
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#
# # Create a DataFrame
# movies = pd.DataFrame(movies_dict)
#
# # Load the similarity matrix
# similarity_distance = pickle.load(open('similarity_distance.pkl', 'rb'))
#
# # Title of the Streamlit app
# st.title('Movie Recommendation System')
#
# # Dropdown for selecting a movie
# selected_movie_name = st.selectbox(
#     "!---Here Your movie---!?",
#     movies['title'].values
# )
#
# # Button to recommend movies
# if st.button('Recommend'):
#     names, poster = Recommended(selected_movie_name, similarity_distance)
#
#     # Display recommendations in columns
#     cols = st.columns(10)  # Create 10 columns dynamically
#
#     for i, col in enumerate(cols):
#         with col:
#             if i < len(names):  # Ensure no index out of range errors
#                 st.text(names[i])
#                 st.image(poster[i])



# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movies_id):
#     url = f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()
#
#         # Check if 'poster_path' exists in the response
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Return a placeholder image if 'poster_path' is not available
#             return "https://via.placeholder.com/500x750?text=No+Image"
#     except requests.exceptions.RequestException as e:
#         # Handle any errors in the API request gracefully
#         st.error(f"Error fetching poster: {e}")
#         return "https://via.placeholder.com/500x750?text=No+Image"
#
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
#         movies_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movies_id))  # Append movie poster
#     return Recommende_movies, Recommende_movies_poster
#
#
# # Load the movie dictionary
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#
# # Create a DataFrame
# movies = pd.DataFrame(movies_dict)
#
# # Load the similarity matrix
# similarity_distance = pickle.load(open('similarity_distance.pkl', 'rb'))
#
# # Title of the Streamlit app
# st.title('Movie Recommendation System')
#
# # Dropdown for selecting a movie
# selected_movie_name = st.selectbox(
#     "!---Here Your movie---!?",
#     movies['title'].values
# )
#
# # Button to recommend movies
# if st.button('Recommend'):
#     names, poster = Recommended(selected_movie_name, similarity_distance)
#
#     # Display recommendations in responsive columns (max 5 per row)
#     st.markdown("""
#     <style>
#     .row .column {
#         display: flex;
#         flex-wrap: wrap;
#     }
#     @media (max-width: 600px) {
#         .column {
#             width: 100%;
#         }
#     }
#     @media (min-width: 600px) {
#         .column {
#             width: 50%;
#         }
#     }
#     @media (min-width: 1000px) {
#         .column {
#             width: 20%;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)
#
#     # Create dynamic columns based on the screen size
#     for i in range(0, len(names), 5):  # Group movies into sets of 5 for rows
#         cols = st.columns(5)  # 5 columns per row
#         for j, col in enumerate(cols):
#             if i + j < len(names):  # Ensure we don't go out of range
#                 with col:
#                     st.text(names[i + j])  # Display movie title
#                     st.image(poster[i + j])  # Display movie poster


# BAda front size wala hai ye
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movies_id):
#     url = f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()
#
#         # Check if 'poster_path' exists in the response
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Return a placeholder image if 'poster_path' is not available
#             return "https://via.placeholder.com/500x750?text=No+Image"
#     except requests.exceptions.RequestException as e:
#         # Handle any errors in the API request gracefully
#         st.error(f"Error fetching poster: {e}")
#         return "https://via.placeholder.com/500x750?text=No+Image"
#
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
#         movies_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movies_id))  # Append movie poster
#     return Recommende_movies, Recommende_movies_poster
#
#
# # Load the movie dictionary
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#
# # Create a DataFrame
# movies = pd.DataFrame(movies_dict)
#
# # Load the similarity matrix
# similarity_distance = pickle.load(open('similarity_distance.pkl', 'rb'))
#
# # Title of the Streamlit app
# st.title('Movie Recommendation System')
#
# # Dropdown for selecting a movie
# selected_movie_name = st.selectbox(
#     "!---Here Your movie---!?",
#     movies['title'].values
# )
#
# # Button to recommend movies
# if st.button('Recommend'):
#     names, poster = Recommended(selected_movie_name, similarity_distance)
#
#     # Display recommendations in responsive grid (5 per row)
#     st.markdown("""
#     <style>
#     /* CSS Grid layout for 5 posters in a row */
#     .movie-container {
#         display: grid;
#         grid-template-columns: repeat(5, 1fr);  /* 5 columns in a row */
#         gap: 20px;
#         margin-top: 20px;
#     }
#
#     .movie-item {
#         text-align: center;
#         background-color: #f4f4f4;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#
#     .movie-item img {
#         max-width: 100%;
#         height: auto;
#         border-radius: 8px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#
#     .movie-item h4 {
#         margin-top: 10px;
#         font-size: 14px;
#         color: #333;
#         font-weight: bold;
#     }
#
#     /* Responsive design adjustments */
#     @media (max-width: 600px) {
#         .movie-container {
#             grid-template-columns: repeat(1, 1fr);  /* 1 column per row */
#         }
#     }
#
#     @media (min-width: 600px) and (max-width: 1000px) {
#         .movie-container {
#             grid-template-columns: repeat(2, 1fr);  /* 2 columns per row */
#         }
#     }
#
#     @media (min-width: 1000px) {
#         .movie-container {
#             grid-template-columns: repeat(5, 1fr);  /* 5 columns per row */
#         }
#     }
#
#     </style>
#     """, unsafe_allow_html=True)
#
#     # Create a container for movie posters and titles
#     st.markdown('<div class="movie-container">', unsafe_allow_html=True)
#
#     # Loop through the names and posters and display them in a grid layout
#     for i in range(len(names)):
#         st.markdown(f"""
#         <div class="movie-item">
#             <img src="{poster[i]}" alt="{names[i]}">
#             <h4>{names[i]}</h4>
#         </div>
#         """, unsafe_allow_html=True)
#
#     st.markdown('</div>', unsafe_allow_html=True)



# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movies_id):
#     url = f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()
#
#         # Check if 'poster_path' exists in the response
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Return a placeholder image if 'poster_path' is not available
#             return "https://via.placeholder.com/500x750?text=No+Image"
#     except requests.exceptions.RequestException as e:
#         # Handle any errors in the API request gracefully
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
#         movies_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movies_id))  # Append movie poster
#     return Recommende_movies, Recommende_movies_poster
#
# # Load the movie dictionary
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#
# # Create a DataFrame
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
# # Button to recommend movies
# if st.button('Recommend'):
#     names, poster = Recommended(selected_movie_name, similarity_distance)
#
#     # Injecting CSS for styling
#     st.markdown("""
#     <style>
#     .movie-container {
#         display: grid;
#         grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));  /* Responsive grid */
#         gap: 20px;
#         margin-top: 20px;
#     }
#
#     .movie-item {
#         text-align: center;
#         background-color: #1c1c1c;
#         color: white;
#         border-radius: 8px;
#         padding: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
#     }
#
#     .movie-item img {
#         max-width: 100%;
#         height: auto;
#         border-radius: 8px;
#     }
#
#     .movie-item h4 {
#         margin-top: 10px;
#         font-size: 14px;
#         color: #fff;
#         font-weight: bold;
#     }
#
#     @media (max-width: 600px) {
#         .movie-container {
#             grid-template-columns: 1fr;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)
#
#     # Create a container for movie posters and titles
#     st.markdown('<div class="movie-container">', unsafe_allow_html=True)
#
#     # Loop through the names and posters and display them in a grid layout
#     for i in range(len(names)):
#         st.markdown(f"""
#         <div class="movie-item">
#             <img src="{poster[i]}" alt="{names[i]}">
#             <h4>{names[i]}</h4>
#         </div>
#         """, unsafe_allow_html=True)
#
#     st.markdown('</div>', unsafe_allow_html=True)

## this is correct which i need
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#
#         # Check if 'poster_path' exists and return full poster URL
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Return a placeholder image if poster_path is unavailable
#             return "https://via.placeholder.com/500x750?text=No+Image+Available"
#     except requests.exceptions.RequestException as e:
#         # Handle any errors while fetching poster
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
#     # Find the index of the selected movie
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity_distance[movie_index]
#
#     # Get the top 10 most similar movies (excluding the selected one)
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
#
#     Recommende_movies = []
#     Recommende_movies_poster = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movie_id))  # Append movie poster URL
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
# # Button to recommend movies
# if st.button('Recommend'):
#     names, posters = Recommended(selected_movie_name, similarity_distance)
#
#     # Display movies in rows with 5 columns each
#     for i in range(0, len(names), 5):  # Iterate in chunks of 5
#         cols = st.columns(5)  # Create 5 columns
#         for col, name, poster in zip(cols, names[i:i+5], posters[i:i+5]):
#             with col:
#                 st.image(poster, use_container_width=True)  # Display poster using updated parameter
#                 st.text(name)  # Display movie name
#
#


## user slier wala
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch the poster of the movie using its ID
# def fetchPoster(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2981ba02f85806064b99326e99dfe944&language=en-US'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#
#         # Check if 'poster_path' exists and return full poster URL
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
#     # Find the index of the selected movie
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity_distance[movie_index]
#
#     # Get the top 10 most similar movies (excluding the selected one)
#     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
#
#     Recommende_movies = []
#     Recommende_movies_poster = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id  # Fetch movie ID
#         Recommende_movies.append(movies.iloc[i[0]].title)  # Append movie title
#         Recommende_movies_poster.append(fetchPoster(movie_id))  # Append movie poster URL
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
# # Slider to choose the number of movies per row
# movies_per_row = st.slider("Movies Per Row", min_value=1, max_value=10, value=5, step=1)
#
# # Button to recommend movies
# if st.button('Recommend'):
#     names, posters = Recommended(selected_movie_name, similarity_distance)
#
#     # Display movies in rows based on user input
#     for i in range(0, len(names), movies_per_row):  # Iterate in chunks of the chosen row size
#         cols = st.columns(movies_per_row)  # Create dynamic columns
#         for col, name, poster in zip(cols, names[i:i+movies_per_row], posters[i:i+movies_per_row]):
#             with col:
#                 st.image(poster, use_container_width=True)  # Display poster using updated parameter
#                 st.text(name)  # Display movie name


## user filter wala
import streamlit as st
import pickle
import pandas as pd
import requests

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
                st.text(name)  # Display movie name

## YAD WATCHLIST M ADD KRNE K LIYE H
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
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
#                 st.text(name)  # Display movie name
#
#                 # Add options below each movie
#                 action = st.selectbox(
#                     f"Options for {name}",
#                     ["Choose an option", "Add to Watchlist", "View Details", "Rate this Movie"],
#                     key=f"action_{name}"  # Unique key for each movie
#                 )
#
#                 # Perform actions based on user selection
#                 if action == "Add to Watchlist":
#                     st.success(f"Added {name} to your watchlist! 🎉")
#                 elif action == "View Details":
#                     st.info(f"Viewing details for {name}... (Feature in progress 🚀)")
#                 elif action == "Rate this Movie":
#                     rating = st.slider(f"Rate {name} (1-5):", 1, 5, key=f"rating_{name}")
#                     st.success(f"Thank you for rating {name}: {rating} stars! ⭐")


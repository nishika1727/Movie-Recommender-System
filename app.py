import streamlit as st
import pickle
import pandas as pd
import requests

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetchposter(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ea159aac6405136cd327091d926b32c3&language=en-US',
            timeout=5  # timeout in seconds
        )
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return 'https://image.tmdb.org/t/p/original/' + poster_path
        else:
            return 'https://via.placeholder.com/300x450?text=No+Image'
    except requests.exceptions.Timeout:
        return 'https://via.placeholder.com/300x450?text=Timeout'
    except Exception as e:
        return 'https://via.placeholder.com/300x450?text=Error'


def recommend(movie):
    ind = movies[movies['title'] == movie].index[0]
    distances = similarity[ind]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movieId = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetchposter(movieId))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    movies['title']
)

if st.button('Recommend'):
    names, poster = recommend(selected_movie)

    # for i in names:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[0])
        st.image(poster[0])
    with col2:
        st.write(names[1])
        st.image(poster[1])
    with col3:
        st.write(names[2])
        st.image(poster[2])
    with col4:
        st.write(names[3])
        st.image(poster[3])
    with col5:
        st.write(names[4])
        st.image(poster[4])
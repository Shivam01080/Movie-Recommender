import streamlit as st
import pickle as pkl
import requests

movies = pkl.load(open("movies.pkl", "rb"))
similarity = pkl.load(open("similarity.pkl", "rb"))


def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e6e0c0d828e70b33c5797a048eb6f8ed")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    movie_poster = []
    ratings = []
    for j in movie_list:
        movie_id = movies.iloc[j[0]].movie_id
        recommended_movies.append(movies.iloc[j[0]].title)
        movie_poster.append(fetch_poster(movie_id))
        ratings.append(movies.iloc[j[0]].vote_average)
    return recommended_movies, movie_poster, ratings


st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎥 Movie Recommender System")
st.header("Welcome to an immersive experience to discover your next favorite movie!")

option = st.selectbox(
    "Type the name or select from the list",
    movies['title'].values)
if st.button("Recommend"):
    names, poster, stars = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
        st.subheader(f"Rating : {stars[0]}/10")
    with col2:
        st.text(names[1])
        st.image(poster[1])
        st.subheader(f"Rating : {stars[1]}/10")
    with col3:
        st.text(names[2])
        st.image(poster[2])
        st.subheader(f"Rating : {stars[2]}/10")
    with col4:
        st.text(names[3])
        st.image(poster[3])
        st.subheader(f"Rating : {stars[3]}/10")
    with col5:
        st.text(names[4])
        st.image(poster[4])
        st.subheader(f"Rating : {stars[4]}/10")

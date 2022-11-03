import pickle
import streamlit as st
import requests

st.header("Welcome to INDIAN MOVIES RECOMMENDER")
movies = pickle.load(open('MOVIE_RECOMMENDATION/movie_list_indian.pkl','rb'))
similarity = pickle.load(open('MOVIE_RECOMMENDATION//similarity_indian.pkl','rb'))

##movie select option
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)



##background image
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('MOVIE_RECOMMENDATION/2.png')



##poster fetch
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

##movie recommend
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:10]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        print(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        
    return recommended_movie_names,recommended_movie_posters
        
##recommend button and suggestion        
if st.button('Show Recommendation'):
    width_value = 250
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3= st.columns([1,1,1],gap='large')
    with col1:
        st.markdown(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],use_column_width='never',width=width_value)
    with col1:
        st.markdown(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],use_column_width='never',width=width_value)
    with col1:
        st.markdown(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],use_column_width='never',width=width_value)        
    with col2:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],use_column_width='never',width=width_value)
    with col2:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],use_column_width='never',width=width_value)
    with col2:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5],use_column_width='never',width=width_value)
    with col3:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6],use_column_width='never',width=width_value)
    with col3:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7],use_column_width='never',width=width_value)
    with col3:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8],use_column_width='never',width=width_value)
import streamlit as st
import pickle
import requests

#-------------------Importing Data-----------------------#
@st.cache_data 
def load_data():

    movie_data = pickle.load(open('movies_dataset.pickle', 'rb'))
    movie_names=movie_data['title'].values
    similarity = pickle.load(open('similarity.pickle', 'rb'))
    return movie_data,movie_names, similarity

API_key="0e841cdee64c29bc46baaf338d827d80"

@st.cache_data 
def fetch_poster(movie_id,api_key):
    response=requests.get("http://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,api_key))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

@st.cache_data 
def recommend(movie,movies_df,similarity):
    movie_index=movies_df[movies_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recom_list=[]
    recom_posters=[]
    for i in movies_list:
        recom_list.append(movies_df.iloc[i[0]].title)
        recom_posters.append(fetch_poster(movies_df.iloc[i[0]].movie_id,api_key=API_key))
    return recom_list,recom_posters

#------------------------Creating webpage---------------#
st.image('movie_image.jpg')
st.write(" ")
st.title('Movie Recommender System')
st.write(" ")

home,info=st.tabs(['Home','Info'])

#----------------------Home_Tabe-------------------------#
with home:
    movie_data,movie_names,similarity=load_data()
    name=st.selectbox('Enter Movie Name',movie_names)
    
    
    
    if "load_state" not in st.session_state:
        st.session_state.load_state=False
        
        
    if st.button("Recommend") or st.session_state.load_state:
        st.session_state.load_state=True
        
        st.subheader('Recommendations:')
        
        recommended,posters=recommend(name,movie_data,similarity)
        
        columns=st.columns(len(recommended))
        column_width = 225
        column_height = 300
        
        
        for i in range(len(recommended)):
            
            columns[i].image(posters[i], caption=recommended[i], width=column_width, use_column_width=True)
            button_key=f"button_{recommended[i]}_{i}"
                        
  
#-----------------------------INFO_Tab------------------------#

with info:
    st.write("""
             Movie Recommendation System Credits:

Data Source:

Movie data used in this recommendation system is sourced from TMDB (The Movie Database).
[TMDB](https://www.themoviedb.org/?language=en-US) is an online database that provides comprehensive information about movies, TV shows, and actors.

TMDB Dataset Credits:

The Movie Database (TMDB) API: https://www.themoviedb.org/documentation/api
TMDB Dataset: https://www.themoviedb.org/documentation/api

Disclaimer:

This recommendation system is built using data from TMDB, and all credit for the underlying movie information goes to TMDB and its contributors.
Acknowledgments:

We extend our gratitude to the TMDB community and contributors for maintaining a rich and up-to-date database of movie information.
             
             """)      
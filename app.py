import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.title("Movie Recommender system")
st.subheader("Your choices matters ")
st.write("""ABOUT US\n
You are at the right place!Here you can fill all your movie watching dreams!!!\n
Online movie recommendations offers many types of movies together to fulfill readers requirements based on their interests.\n
This system also provide popular recommendations so user can get right popular choices.""")
from PIL import Image
image=Image.open("img_1.png")
st.image(image,caption="All types of movies are available")
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))
title_list=movies_list['original_title'].values
cast_list=movies_list['cast'].values
crew_list=movies_list['crew'].values
user_list=movies_list['user_id'].values
genre_list=movies_list['genres'].values
st.subheader(""" Explore different types of movies based on your interests """)
option=st.selectbox('select the option',('original_title','cast','crew','user_id','genres'))
def unique(genre_list):
    unique_list=[]
    for x in genre_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
def icst(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
            return i
    return -1

movies['user_id']=movies['user_id'].astype(str)
def recommend(movie):
    if option == 'cast':
        recommended_movie_names = []
        dex = []  
        for i, s in enumerate(movies['cast']):
            if movie in s:
                cast_index = i
                m = (movies.iloc[i].original_title)
                dex.append(m)
        n = len(dex[0:5])
        idex = '\n'.join(dex[0:5])
        distances = similarity[cast_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6 -n]
        for i in movies_list:
            idex = idex + '\n' + (movies.iloc[i[0]].original_title)
        recommended_movie_names = idex.split('\n')
        return recommended_movie_names
    elif option=='crew':
        recommended_movie_names = []
        dex = []
        for i, s in enumerate(movies['crew']):
            if movie in s:
                crew_index = i
                m = (movies.iloc[i].original_title)
                dex.append(m)
        n = len(dex[0:5])
        idex = '\n'.join(dex[0:5])
        distances = similarity[crew_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6 -n]
        for i in movies_list:
            idex = idex + '\n' + (movies.iloc[i[0]].original_title)
            recommended_movie_names = idex.split('\n')
        return recommended_movie_names
    elif option == 'original_title':
        movie_index = movies[movies['original_title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies= []
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]].original_title)
            return recommended_movies
    elif option=='user_id':
        user_index = icst(movies['user_id'], movie)
        distances = similarity[user_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]].original_title)
        return recommended_movies
    elif option=='genres':
        recommended_movie_names = []
        dex = []
        for i, s in enumerate(movies['genres']):
            if movie in s:
                genres_index = i
                m = (movies.iloc[i].original_title)
                dex.append(m)
        n = len(dex[0:5])
        idex = '\n'.join(dex[0:5])
        distances = similarity[genres_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6 -n]
        for i in movies_list:
            idex = idex + '\n' + (movies.iloc[i[0]].original_title)
            recommended_movie_names = idex.split('\n')
        return recommended_movie_names
st.write('You selected:', option)
if(option=='original_title'):
    selected_choice = st.selectbox("select a title from the dropdown",title_list)
if(option=='cast'):
    selected_choice = st.selectbox("select a cast from the dropdown",cast_list)
if(option=='crew'):
    selected_choice = st.selectbox("select a crew from the dropdown",crew_list)
if(option=='user_id'):
    selected_choice=st.selectbox("select a user_id from the dropdown",user_list)
if(option=='genres'):
    selected_choice=st.selectbox("select a user_id from the dropdown",unique(genre_list))
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_choice)
    for i in recommended_movie_names:
        st.write(i)
if st.sidebar.button("Popular recommendations "):
    st.sidebar.write("Popular recommendations for the movies ")
    popular_movies_list = pickle.load(open('popular.pkl', 'rb'))
    popular_movies = pd.DataFrame(popular_movies_list)
    x = popular_movies_list["original_title"].values
    st.sidebar.write("Popular recommendations")
    st.sidebar.write(x)
import streamlit as st
import pickle
import pandas as pd
import os
import gdown

# Replace with your actual Google Drive file IDs
movie_dict_id = '13aT_dmzlvUoOkiPUBuvIBTGDhhcBk01R'
similarity_id = '1N394vQ_qJxaudSxIYMYWDEwNTNmd9uQw'

def download_file_from_drive(file_id, output_name):
    if not os.path.exists(output_name):
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url=url, output=output_name, fuzzy=True, quiet=False)

# Download the files
download_file_from_drive(movie_dict_id, 'movie_dict.pkl')
download_file_from_drive(similarity_id, 'similarity.pkl')

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('What to watch?', movies['title'].values)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

if st.button("Recommend"):
    for name in recommend(selected_movie_name):
        st.write(name)

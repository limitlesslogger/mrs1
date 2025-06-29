# import streamlit as st
# import pickle
# import pandas as pd
# movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# similarity=pickle.load(open('similarity.pkl','rb'))
# movies=pd.DataFrame(movies_dict)
# st.title('Movie Reccomender System')
# selected_movie_name=st.selectbox('What to watch?',movies['title'].values)
# def recommend(movie):
#     movie_index=movies[movies['title'] == movie].index[0]
#     distances=similarity[movie_index]
#     movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
#     recommended_movies=[]
#     for i in movies_list:
#         # movie_id=i[0]
#         # fetch poster from api
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
# if st.button("Recommend"):
#     recommendations=recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)

import streamlit as st
import pickle
import pandas as pd
import os
import gdown

# Replace with your actual file IDs from Google Drive
movie_dict_id = 'YOUR_MOVIE_DICT_ID'
similarity_id = 'YOUR_SIMILARITY_ID'

def download_file(file_id, output):
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

# Download .pkl files if not already downloaded
download_file(movie_dict_id, '13aT_dmzlvUoOkiPUBuvIBTGDhhcBk01R')
download_file(similarity_id, '1N394vQ_qJxaudSxIYMYWDEwNTNmd9uQw')

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

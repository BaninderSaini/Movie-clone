import requests
import pickle
import streamlit as st


def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=#####&language=en-US".format(movie_id)
    dataset = requests.get(url)
    dataset = dataset.json()
    poster_path = dataset['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def overview(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=#####&language=en-US".format(movie_id)
    dataset = requests.get(url)
    data = dataset.json()

    return data['overview']
def ratings(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=#####&language=en-US".format(
        movie_id)
    dataset = requests.get(url)
    dataset = dataset.json()

    return (str(dataset['vote_average'])+' /10')
def language(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=#####&language=en-US".format(
        movie_id)
    dataset = requests.get(url)
    dataset = dataset.json()
    return dataset['spoken_languages'][0]['english_name']

def recommend(movie):
    i = m[m['title'] == movie].index[0]
    distances = sorted(list(enumerate(s[i])), reverse=True, key=lambda x: x[1])
    movie_names = []
    movie_posters = []
    overview_movie=[]
    vote_avg=[]
    languages=[]
    for i in distances[0:6]:

        movie_id = m.iloc[i[0]].tmdbId
        movie_posters.append(poster(movie_id))
        movie_names.append(m.iloc[i[0]].title)
        overview_movie.append(overview(movie_id))
        vote_avg.append(ratings(movie_id))
        languages.append(language(movie_id))


    return movie_names,movie_posters,overview_movie,vote_avg,languages

_, a, _ = st.columns([1, 2, 1])
with a:
    st.title('Unlimited Movies for You ')
st.header('Watch anytime from anywhere')

m = pickle.load(open('movieNames.pkl','rb'))
s = pickle.load(open('others.pkl','rb'))

movie_list = m['title'].values



selected_movie = st.selectbox(
"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
movie_list
)



if st.button('GO'):
      movie_names,movie_posters,overview_movie,vote_avg,languages = recommend(selected_movie)
      cl1,cl2=st.columns(2)
      with cl1:
        st.image(movie_posters[0],width=400)
      with cl2:
        st.title(movie_names[0])
        st.header('Overview')
        st.text(overview_movie[0])

        st.text('')
        st.text('')
        st.header("Language")
        st.text(languages[0])
        st.text('')
        st.header('Ratings')
        st.text(vote_avg[0])


        st.text('')
        st.button('Watch')


      col1, col2, col3, col4, col5 = st.columns(5)
      with col1:
        st.text(movie_names[1])
        st.image(movie_posters[1])
        st.text(vote_avg[1])

      with col2:
        st.text(movie_names[2])
        st.image(movie_posters[2])
        st.text(vote_avg[2])

      with col3:
        st.text(movie_names[3])
        st.image(movie_posters[3])
        st.text(vote_avg[3])
      with col4:
        st.text(movie_names[4])
        st.image(movie_posters[4])
        st.text(vote_avg[4])
      with col5:
        st.text(movie_names[5])
        st.image(movie_posters[5])
        st.text(vote_avg[5])

_, b, _ = st.columns([1.2, 2, 1])
with b:
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.text('Copyright © 2020-2030 watch #fun')

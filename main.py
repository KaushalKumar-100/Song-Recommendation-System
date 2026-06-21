import streamlit as st
import requests
import pickle
import json

st.set_page_config(
    page_title="Song Recommendation",

    initial_sidebar_state="expanded",)

with open('music.pkl', 'rb') as f:
    music=pickle.load(f)
# music=pickle.load(open("music.pkl", "rb"))
similarity=pickle.load(open("Surrounding.pkl", "rb"))
st.title("🎶Get All your favourite songs")




music_list=[]
for key,value in music['album_name'].items():
    music_list.append((key,value))
selected_music=st.selectbox("Select your genre music or album",music_list,format_func=lambda x:x[1])

# url="https://www.youtube.com/search"
# response=requests.get(url,params={"q":selected_music[0]})
# print(response.json())
def fetch_poster2(index):
    try:
        song_name = music['album_name'][index]
        url="https://itunes.apple.com/search"
        params={
            'term':song_name,
            'entity':"song",
            "limit":1
        }
        response=requests.get(url,params=params,timeout=8)
        data=response.json()
        if data['resultCount']>0:
            result=data['results'][0]
            poster_url=result['artworkUrl100']
            poster_url=poster_url.replace("100x100","600x600")
            preview=result.get('previewUrl')
            poster_link=poster_url
        else:
            poster_link=None
            preview=None
    except Exception as e:
        print("ERROR:", e)
        poster_link=None
        preview=None
    return poster_link, preview



def recommended(selected_music):
    music_index=selected_music[0]
    music_list_index =[x[0] for x in similarity[music_index]]
    recommended_music_name=[]


    for i in music_list_index:
        recommended_music_name.append(music['album_name'][i])


    return recommended_music_name,music_list_index


# st.session_state.sidebar.text_input("Enter your Name:"


name=st.sidebar.text_input("Enter your name:")
st.session_state['name']=name


# if st.button(load_history):

if 'search_history' not in st.session_state:
    st.session_state.search_history=[]
current_poster,audio=fetch_poster2(selected_music[0])

if st.button("Similar Song"):
    with st.spinner("Loading similar song"):

        names,music_list_index=recommended(selected_music)
        poster=[]
        preview=[]
        for fetch in music_list_index:
            image,audio=fetch_poster2(fetch)
            poster.append(image)
            preview.append(audio)




    a=selected_music[1]
    if a not in st.session_state.search_history:
        st.session_state.search_history.append(a)


    for row in range(3):
        cols=st.columns(3)
        for col in range(3):
            index=row*3+col
            with cols[col]:
                st.text(names[index])
                if poster[index]:
                    st.image(poster[index],width=200)
                else:
                    st.write("no image Available")
                if preview[index]:
                    st.audio(preview[index])
                else:
                    st.write("no audio Available")



with st.sidebar.expander("Searched History",expanded=True):
    for song in st.session_state.search_history:
        st.write(song)


st.sidebar.image(current_poster,width=200)
st.sidebar.audio(audio)


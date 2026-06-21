# 🎵 Song Recommendation System


A machine learning-based music recommendation web application that suggests similar songs based on content similarity. The application provides album artwork, 30-second audio previews, and maintains a user's recent search history using Streamlit session state.

---

## 🌐 Live Demo

🔗 https://song-recommendation-system-100.streamlit.app/

---

## 📌 Features

- 🎧 Get song recommendations based on selected songs
- 🖼️ Display high-quality album artwork
- ▶️ Listen to 30-second song previews
- 🔎 Search songs through an interactive dropdown
- 📝 View recently searched songs
- ⚡ Fast recommendations using precomputed similarity data
- 💻 Clean and responsive Streamlit user interface
- 🌍 Fetch real-time music details using iTunes Search API

---

## 🧠 How It Works

1. The user selects a song from the dropdown.
2. The application finds the selected song's index.
3. A precomputed similarity matrix is used to find similar songs.
4. Recommended song names are retrieved from the dataset.
5. The iTunes Search API is called to fetch:
   - Album artwork
   - 30-second audio preview
6. The recommendations are displayed in a grid layout.



## 🛠️ Technologies Used

### Machine Learning
- Python
- Pandas
- Pickle
- Cosine Similarity


### API Integration
- iTunes Search API
- Requests library

## 📊 Dataset Information

The project uses a music dataset containing:

- Track ID
- Album Name
- Genre/Tags

The recommendation model uses content-based filtering with similarity scores generated using machine learning techniques.




## 👨‍💻 Author

**Kaushal Kumar**

- GitHub: https://github.com/KaushalKumar-100


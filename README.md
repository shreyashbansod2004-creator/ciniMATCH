# 🎬 CineMatch – AI-Powered Movie Recommendation System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red.svg" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Recommender%20System-green.svg" />
  <img src="https://img.shields.io/badge/TMDB-API-orange.svg" />
</p>

## 🚀 Live Demo

**Try CineMatch Here:**

https://cinimatch-ujat8qzrg8zaiipevvnzsq.streamlit.app/

---

# 📌 Overview

CineMatch is an AI-powered movie recommendation system that helps users discover movies similar to the ones they already enjoy.

Using Machine Learning and content-based filtering techniques, the application analyzes movie features and generates personalized recommendations based on similarity scores.

The project combines recommendation algorithms, movie metadata analysis, TMDB integration, and an interactive Streamlit interface to create a complete end-to-end recommendation platform.

---

# ✨ Features

* 🎬 Movie recommendation engine
* 🤖 Machine Learning powered similarity matching
* 🔍 Search and select movies instantly
* 🖼️ Dynamic movie posters fetched using TMDB API
* ⚡ Fast recommendation generation
* 🌐 Fully deployed Streamlit application
* 🎨 Modern custom-designed UI
* 📱 Responsive user experience

---

# 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Content-Based Recommendation System
* Cosine Similarity

### Data Processing

* Pandas
* NumPy

### Frontend

* Streamlit
* Custom CSS

### APIs

* TMDB (The Movie Database API)

### Deployment

* Streamlit Cloud

---

# 🧠 How It Works

The recommendation engine follows a Content-Based Filtering approach.

### Step 1: Data Collection

Movie information such as:

* Title
* Genres
* Keywords
* Cast
* Crew
* Overview

is collected and processed.

---

### Step 2: Feature Engineering

Relevant movie attributes are combined into a single feature representation.

Example:

Action + Adventure + Sci-Fi + Christopher Nolan + Space

This allows movies with similar characteristics to be compared effectively.

---

### Step 3: Similarity Matrix Creation

A similarity matrix is generated using machine learning techniques.

Each movie receives a similarity score against every other movie in the dataset.

---

### Step 4: Recommendation Generation

When a user selects a movie:

1. The movie is located in the dataset.
2. Similarity scores are retrieved.
3. Top matching movies are ranked.
4. Top recommendations are displayed.

---

# 🎯 Recommendation Pipeline

User Selects Movie

↓

Feature Extraction

↓

Similarity Matrix Lookup

↓

Top Similar Movies

↓

TMDB Poster Fetching

↓

Recommendations Displayed

---

# 📊 Example

### User Input

Interstellar

### Recommendations

* The Martian
* Gravity
* Inception
* Contact
* Moon

*(Recommendations vary based on model data.)*

---

# 📷 Application Screenshots

## Home Page

Add screenshot here:

```md
![Homepage](screenshots/homepage.png)
```

## Recommendation Results

```md
![Recommendations](screenshots/recommendations.png)
```

---

# 📂 Project Structure

```bash
CineMatch/
│
├── app.py
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── Movie_Recommendation_System.ipynb
│
├── screenshots/
│   ├── homepage.png
│   └── recommendations.png
│
├── movie_dict.pkl
└── similarity.pkl
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/CineMatch.git
```

### Navigate to Project Folder

```bash
cd CineMatch
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 💡 Key Learnings

This project helped develop skills in:

* Recommendation Systems
* Machine Learning
* Feature Engineering
* Similarity Analysis
* API Integration
* Data Processing
* Streamlit Deployment
* User Interface Design
* End-to-End ML Application Development

---

# 🌍 Real-World Applications

Recommendation systems are widely used in:

* Netflix
* Amazon Prime Video
* Disney+
* Spotify
* YouTube
* E-commerce platforms

This project demonstrates the core concepts behind modern recommendation engines used by large-scale platforms.

---

# 🔮 Future Improvements

* Hybrid Recommendation System
* Collaborative Filtering
* Deep Learning-Based Recommendations
* User Profiles & Personalization
* Watch History Tracking
* Movie Ratings Integration
* Genre-Based Filtering
* User Authentication

---

# 🏆 Project Highlights

✅ End-to-End Machine Learning Project

✅ Real-Time Recommendations

✅ TMDB API Integration

✅ Public Deployment

✅ Modern UI Design

✅ Recruiter-Friendly Portfolio Project

---

# 👨‍💻 Author

### Shreyash Bansod

Data Science Student | Machine Learning Enthusiast

Interested in:

* Data Science
* Machine Learning
* Recommendation Systems
* NLP
* Generative AI
* AI Applications

---

⭐ If you found this project useful, consider giving it a star on GitHub.

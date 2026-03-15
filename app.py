import os
import gdown
import pandas as pd
import streamlit as st
import pickle
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="CineMatch — Shreyash Bansod",
    page_icon="🎬",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@300;400;500;600&display=swap');

:root {
  --bg:     #080d0a;
  --bg2:    #0c1410;
  --card:   #111a14;
  --green:  #9CFF00;
  --cyan:   #00ffe0;
  --text:   #e6f5ec;
  --muted:  #7da890;
  --border: rgba(156,255,0,0.15);
  --glow:   rgba(156,255,0,0.25);
}

html, body, [class*="css"] {
  background-color: var(--bg);
  color: var(--text);
  font-family: 'Poppins', sans-serif;
}

body::before {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 0; opacity: 0.35;
}

.stApp::before {
  content: '';
  position: fixed; inset: 0;
  background-image:
    linear-gradient(rgba(156,255,0,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(156,255,0,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: gridShift 20s linear infinite;
  z-index: 0; pointer-events: none;
}
@keyframes gridShift {
  0% { background-position: 0 0; }
  100% { background-position: 60px 60px; }
}

.stApp::after {
  content: '';
  position: fixed;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(156,255,0,0.07) 0%, transparent 70%);
  top: -150px; right: -100px;
  border-radius: 50%; filter: blur(80px);
  pointer-events: none; z-index: 0;
  animation: blobFloat 8s ease-in-out infinite;
}
@keyframes blobFloat {
  0%,100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-30px) scale(1.05); }
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 4rem; max-width: 1400px; position: relative; z-index: 2; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--green); border-radius: 2px; }

.progress-bar {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--green), var(--cyan));
  box-shadow: 0 0 8px var(--green);
  z-index: 9999; width: 100%;
  animation: progressLoad 1.5s ease forwards;
}
@keyframes progressLoad { from { width: 0%; } to { width: 100%; } }

.hero { text-align: center; padding: 3rem 0 2rem; position: relative; }
.hero-label {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 5px 16px; border: 1px solid var(--border); border-radius: 30px;
  font-size: 11px; color: var(--green); letter-spacing: 2px;
  text-transform: uppercase; background: rgba(156,255,0,0.04);
  margin-bottom: 16px; animation: labelPulse 3s ease-in-out infinite;
}
@keyframes labelPulse {
  0%,100% { box-shadow: 0 0 0 rgba(156,255,0,0); }
  50% { box-shadow: 0 0 15px rgba(156,255,0,0.1); }
}
.hero-label .dot {
  width: 6px; height: 6px; background: var(--green); border-radius: 50%;
  box-shadow: 0 0 6px var(--green);
  animation: dotBlink 1.5s ease-in-out infinite; display: inline-block;
}
@keyframes dotBlink { 0%,100%{opacity:1} 50%{opacity:0.2} }

.hero h1 {
  font-family: 'Anton', sans-serif;
  font-size: clamp(3rem, 8vw, 6rem);
  background: linear-gradient(90deg, #9CFF00, #7dffb3, #ffffff, #9CFF00);
  background-size: 300%;
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  animation: heroGrad 6s linear infinite;
  line-height: 1.05; margin: 0; letter-spacing: 0.05em;
}
@keyframes heroGrad { 0%{background-position:0%} 100%{background-position:300%} }

.hero p { color: var(--muted); font-size: 0.95rem; letter-spacing: 0.2em; text-transform: uppercase; margin-top: 10px; }

.divider {
  width: 100%; height: 1px;
  background: linear-gradient(90deg, transparent, var(--green), transparent);
  position: relative; overflow: visible; margin: 1.8rem 0;
}
.divider::after {
  content: ''; position: absolute; top: -3px; left: 50%; transform: translateX(-50%);
  width: 6px; height: 6px; background: var(--green); border-radius: 50%;
  box-shadow: 0 0 10px var(--green), 0 0 20px var(--green);
}

.section-header { display: flex; align-items: center; gap: 20px; margin-bottom: 40px; }
.section-num-big { font-family: 'Anton', sans-serif; font-size: 80px; color: rgba(156,255,0,0.08); line-height: 1; user-select: none; }
.section-title-wrap h2 { font-family: 'Anton', sans-serif; font-size: 40px; margin-bottom: 5px; color: var(--text); }
.section-title-wrap .line { height: 3px; width: 60px; background: linear-gradient(90deg, var(--green), transparent); border-radius: 2px; }

div[data-testid="stSelectbox"] > div {
  background: var(--card) !important; border: 1px solid var(--border) !important;
  border-radius: 12px !important; color: var(--text) !important;
  font-family: 'Poppins', sans-serif !important;
}
div[data-testid="stSelectbox"] > div:focus-within {
  border-color: var(--green) !important; box-shadow: 0 0 20px var(--glow) !important;
}

div[data-testid="stButton"] > button {
  background: var(--green) !important; color: #000 !important;
  font-family: 'Poppins', sans-serif !important; font-size: 0.95rem !important;
  font-weight: 600 !important; border: none !important; border-radius: 30px !important;
  padding: 0.6rem 2.2rem !important;
  transition: transform 0.3s, box-shadow 0.3s !important; width: 100% !important;
}
div[data-testid="stButton"] > button:hover {
  transform: translateY(-3px) !important; box-shadow: 0 0 20px rgba(156,255,0,0.5) !important;
}

.card-info {
  background: var(--card);
  border: 1px solid var(--border); border-top: none;
  border-radius: 0 0 20px 20px;
  padding: 0.9rem 1rem; margin-top: -4px;
}
.card-rank {
  font-size: 10px; letter-spacing: 2px; text-transform: uppercase;
  color: var(--green); margin-bottom: 5px; font-weight: 600;
}
.card-title {
  font-size: 0.85rem; color: var(--text); font-weight: 500;
  line-height: 1.3; white-space: nowrap; overflow: hidden;
  text-overflow: ellipsis; margin: 0 0 6px 0;
}
.card-tag {
  display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px;
  color: var(--green); border: 1px solid rgba(156,255,0,0.3);
  background: rgba(156,255,0,0.04);
}

div[data-testid="stImage"] > img {
  border-radius: 20px 20px 0 0 !important;
  display: block;
  border: 1px solid var(--border);
  border-bottom: none;
}

div[data-testid="stSpinner"] { color: var(--green) !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-bar"></div>', unsafe_allow_html=True)

# ── TMDB
TMDB_API_KEY  = "5289d836d8b2c4077b568b2c31c4b0ad"
TMDB_IMG_BASE = "https://image.tmdb.org/t/p/w500"

@st.cache_data(show_spinner=False)
def fetch_poster_image(movie_id: int):
    try:
        url  = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        path = resp.json().get("poster_path")
        if path:
            img_url  = TMDB_IMG_BASE + path
            img_resp = requests.get(img_url, timeout=5)
            img_resp.raise_for_status()
            return Image.open(BytesIO(img_resp.content))
    except Exception:
        pass
    return Image.new("RGB", (500, 750), color=(17, 26, 20))

# ── LOAD DATA FROM GOOGLE DRIVE ──────────────────────────────────────────────
@st.cache_resource
def load_data():
    if not os.path.exists("movie_dict.pkl"):
        with st.spinner("Downloading movie data..."):
            gdown.download(
                "https://drive.google.com/uc?id=1WY-xe1lRXgHzS6G9GBZWvQALLcUky-no",
                "movie_dict.pkl", quiet=False
            )
    if not os.path.exists("similarity.pkl"):
        with st.spinner("Downloading similarity model... (this may take a minute)"):
            gdown.download(
                "https://drive.google.com/uc?id=1UKh6VvI8abEVYRMxaWtEUdLpmvhhws8O",
                "similarity.pkl", quiet=False
            )

    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies      = pd.DataFrame(movies_dict)
    similarity  = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

def recommend(movie: str):
    idx       = movies[movies["title"] == movie].index[0]
    distances = similarity[idx]
    top5      = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    names, images = [], []
    for i, _ in top5:
        movie_id = movies.iloc[i]["movie_id"]
        names.append(movies.iloc[i].title)
        images.append(fetch_poster_image(movie_id))
    return names, images

# ── HERO
st.markdown("""
<div class="hero">
  <div class="hero-label"><span class="dot"></span> AI-Powered · ML Recommendations</div>
  <h1>CineMatch</h1>
  <p>Discover your next obsession</p>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ── SEARCH
col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    selected = st.selectbox(
        "Search",
        movies["title"].values,
        label_visibility="collapsed",
        placeholder="Type or select a movie…",
    )
    btn = st.button("Find Recommendations →")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── RESULTS
if btn:
    with st.spinner("Building your watchlist…"):
        names, images = recommend(selected)

    st.markdown("""
    <div class="section-header">
      <span class="section-num-big">03</span>
      <div class="section-title-wrap">
        <h2>Recommended</h2>
        <div class="line"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    cols  = st.columns(5, gap="medium")
    ranks = ["Top Pick", "Pick #2", "Pick #3", "Pick #4", "Pick #5"]
    for idx, col in enumerate(cols):
        with col:
            st.image(images[idx], use_container_width=True)
            st.markdown(f"""
            <div class="card-info">
              <div class="card-rank">{ranks[idx]}</div>
              <p class="card-title">{names[idx]}</p>
              <span class="card-tag">ML Matched</span>
            </div>
            """, unsafe_allow_html=True)
```

Also update your `requirements.txt` to this:
```
streamlit
pandas
requests
scikit-learn
Pillow
gdown

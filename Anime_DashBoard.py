import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "https://api.myanimelist.net/v2"
CLIENT_ID = "your_client_id"


def search_anime(query, limit=10):
    url = f"{API_BASE_URL}/anime"
    headers = {"X-MAL-CLIENT-ID": CLIENT_ID}
    params = {"q": query, "limit": limit}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        st.error("Failed to fetch data. Please check your API key or query.")
        return []

st.title("Anime Dashboard")
st.write("Search for anime and explore details using MyAnimeList API.")


anime_name = st.text_input("Enter Anime Name:", value="Naruto")

if anime_name:
    st.subheader(f"Search Results for '{anime_name}'")
    anime_list = search_anime(anime_name)

    if anime_list:
        for anime in anime_list:
            title = anime["node"]["title"]
            image_url = anime["node"].get("main_picture", {}).get("medium", "")
            st.write(f"### {title}")
            if image_url:
                st.image(image_url, width=150)
    else:
        st.write("No results found.")

st.write("Powered by [MyAnimeList](https://myanimelist.net/).")

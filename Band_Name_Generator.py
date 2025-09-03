#Band_Name_Generator
import random
import streamlit as st

def generate_band_name(words):
    word1 = random.choice(words)
    word2 = random.choice(words)
    while word1 == word2:
        word2 = random.choice(words)
    return f"{word1} {word2}"

st.set_page_config(page_title="Band Name Generator", layout="centered")

st.title("Band Name Generator 🎸🎷🎺")
st.write("---------------------------------")

user_word= st.text_area("Enter some fancy words for your band's name (Minimum 3 words & separated by commas):", "e.g. Rock, Jazz, Blues")

words = [word.strip() for word in user_word.split(",") ]

if st.button("Generate Band Name"):
    st.write("Here are some band names for you:")
    for _ in range(5):
        st.write(generate_band_name(words))
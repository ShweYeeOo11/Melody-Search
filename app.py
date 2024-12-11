import streamlit as st
from modules.emotion_detection import detect_emotion
from modules.song_recommendation import recommend_songs
import pandas as pd
import streamlit.components.v1 as components

# Title
st.title("Melody Search 🎵")
st.write("Find the perfect K-pop song based on your emotions!")

# Debug: Confirm app is running
st.write("Debug: App is running!")

# User input
user_input = st.text_input("How are you feeling today?")
st.write(f"Debug: User input: {user_input}")  # Debugging input

if user_input:
    try:
        # Detect emotion
        emotion = detect_emotion(user_input)
        st.write(f"We detected your emotion as: **{emotion}**")
        st.write(f"Debug: Emotion detected: {emotion}")  # Debugging detected emotion

        # Get song recommendations
        recommendations = recommend_songs(emotion)
        st.write("Here are some song recommendations for you:")

        if recommendations:
            # Limit to 10 songs
            max_songs = 10

            # Allow user to adjust video frame dimensions
            width = st.slider("Set video width", min_value=100, max_value=400, value=800)
            height = st.slider("Set video height", min_value=100, max_value=400, value=450)

            for idx, song in enumerate(recommendations[:max_songs], start=1):  # Show only the first 10 songs
                st.write(f"{idx}. **{song['Song Name']}** by {song['Artist']}")
                # Embed a clickable link
                st.write(f"[Play on YouTube/Spotify]({song['Link']})")
                # Embed video with custom dimensions
                if "youtube" in song['Link']:
                    video_html = f"""
                    <iframe width="{width}" height="{height}" 
                            src="{song['Link'].replace('watch?v=', 'embed/')}" 
                            frameborder="0" allowfullscreen></iframe>
                    """
                    components.html(video_html, height=height + 50)
        else:
            st.error(f"No songs found for emotion '{emotion}'. Check the dataset.")
            # Debug: Load dataset and show relevant content
            dataset = pd.read_csv('data/songs_dataset.csv')
            filtered = dataset[dataset['Emotion'].str.lower() == emotion.lower()]
            st.write(f"Debug: Filtered dataset for emotion '{emotion}':")
            st.write(filtered)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.write(f"Debug: Error details: {e}")  # Debugging unexpected errors

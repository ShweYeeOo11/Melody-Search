import pandas as pd

def recommend_songs(emotion):
    """
    Recommends songs based on the detected emotion.
    """
    # Load the dataset
    dataset = pd.read_csv('data/songs_dataset.csv')

    # Filter songs by emotion (case-insensitive)
    songs = dataset[dataset['Emotion'].str.lower() == emotion.lower()]
    return songs.to_dict('records')


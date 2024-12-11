# **Melody Search 🎵**
![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-orange)

Find the perfect K-pop song based on your emotions! Melody Search is an open-source music recommendation application that combines emotion detection with curated K-pop playlists to create a personalized listening experience.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)
7. [Acknowledgments](#acknowledgments)

---

## **Overview**
Music has the power to resonate with our emotions. Melody Search leverages this by recommending songs based on the user's mood. Whether you're feeling happy, sad, relaxed, or energetic, this app connects you to the best K-pop tracks that match your feelings.

Melody Search uses:
- Machine learning for emotion detection
- Curated playlists of K-pop songs categorized by emotion
- A user-friendly interface powered by Streamlit

---

## **Features**
- **Emotion-Based Recommendations**: Enter how you're feeling, and the app will detect your emotion and recommend songs that match.
- **Dynamic Video Embedding**: Watch recommended songs directly on YouTube with customizable video frame sizes.
- **Curated K-pop Playlists**: Over 20+ K-pop songs categorized into Happy, Sad, Relaxed, and Energetic emotions.
- **Open Source**: Fully customizable and extendable, enabling contributions and modifications.

1. Run the following command to create a virtual environment:
   ```bash
   python -m venv melody_search_env

3. **Install Dependencies**
Install all the required Python libraries for the project:

1. Run the following command to install the dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

## **Installation**

### **Requirements**
To run this project, you need the following:
- Python 3.9 or above
- An internet connection for YouTube links
- A terminal or command prompt to execute commands

### **Steps**
Follow these steps to set up and run the Melody Search project locally:

1. **Clone the Repository**:
   Clone the project repository from GitHub to your local machine:
   ```bash
   git clone https://github.com/yourusername/Melody-Search.git
   cd Melody-Search
2. **Set Up a Virtual Environment**:
   Create a virtual environment to isolate the project's dependencies:
   ```bash
   python -m venv melody_search_env
3. **Install Dependencies**:
   Install all the required Python libraries for the project:

   Run the following command to install the dependencies listed in the `requirements.txt` file:
      ```bash
      pip install -r requirements.txt
4. **Prepare the Dataset**:
   Ensure that the dataset file `songs_dataset.csv` is correctly set up for the application.
5. **Run the Application**:

   1. Ensure your virtual environment is activated. You should see the virtual environment name in your terminal prompt, for example:
      ```
      (melody_search_env) your-computer:Melody-Search user$
      ```

   2. Run the following command to start the Streamlit app:
      ```bash
      streamlit run app.py
      ```

   3. Once the app is running, the terminal will display a URL like this:
      ```
      Local URL: http://localhost:8501
      Network URL: http://192.168.x.x:8501
      ```

   4. Open the `Local URL` in your browser (e.g., `http://localhost:8501`) to access the application.
   
## **Usage**
Follow these steps to use the Melody Search application:

### **1. Enter Your Emotion**
- In the text input box, type how you're feeling. Examples:
  - `"I feel happy"`
  - `"I feel sad"`
  - `"I feel calm"`
  - `"I feel energetic"`
- The application will analyze your input to detect the emotion.

### **2. View Song Recommendations**
- Based on the detected emotion, the app will display a list of songs that match your mood.
- Each song includes:
  - **Title**: The name of the song.
  - **Artist**: The K-pop artist.
  - **Playable Link**: A clickable link to YouTube or Spotify.

### **3. Adjust Video Frame Dimensions**
- Use the sliders in the app to adjust the width and height of embedded YouTube videos.

### **4. Enjoy the Playlist**
- Play songs directly in the app or open them in a new tab using the provided links.

---

## **Technologies Used**
- **Python**: The primary language used for backend development.
- **Streamlit**: For building an interactive web interface.
- **Scikit-learn**: For implementing the emotion detection model.
- **Pandas**: For managing and filtering the song dataset.
- **HTML/CSS**: For embedding videos and customizing the interface.

---

## **Contributing**
We welcome contributions to improve and expand Melody Search. Here's how you can contribute:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name

## **Acknowledgments**
- **Seoul National University of Science and Technology**: For fostering creativity and innovation in software development.
- **K-pop Artists and Fans**: For inspiring the playlists and making this project possible.
- **Streamlit Community**: For providing an easy-to-use framework for building data-driven web apps.
- **Open Source Community**: For inspiring and supporting the development of this project.

## **References**
- [Streamlit Documentation](https://docs.streamlit.io): Comprehensive guide to building web apps using Streamlit.
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html): Reference for machine learning tools used in this project.
- [Pandas Documentation](https://pandas.pydata.org/docs/): Guide for data manipulation and analysis with Pandas.
- [YouTube](https://www.youtube.com): Source for embedding and playing music videos.
- [K-pop Playlist Inspiration](https://kprofiles.com): Inspiration for categorizing K-pop songs by emotion.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Define emotions and example training data
training_data = {
    "happy": ["I feel so joyful", "What a wonderful day", "I am thrilled", "So much fun", "Feeling amazing"],
    "sad": ["I am heartbroken", "I feel lonely", "Such a bad day", "Feeling down", "I am so upset"],
    "relaxed": ["I feel calm", "So peaceful", "I am relaxed", "Such a serene moment", "Enjoying the quiet"],
    "energetic": ["I am full of energy", "Ready to conquer", "Feeling pumped", "So much excitement", "I can't stop moving"]
}

# Prepare the data for training
texts = []
labels = []

for emotion, phrases in training_data.items():
    texts.extend(phrases)
    labels.extend([emotion] * len(phrases))

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a simple Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X, labels)

# Save the model and vectorizer
with open('emotion_model.pkl', 'wb') as model_file:
    pickle.dump((vectorizer, classifier), model_file)

def detect_emotion(user_input):
    """
    Detects the emotion from the user's text input.
    """
    with open('emotion_model.pkl', 'rb') as model_file:
        vectorizer, classifier = pickle.load(model_file)
    
    # Transform user input and predict emotion
    input_vector = vectorizer.transform([user_input])
    prediction = classifier.predict(input_vector)
    return prediction[0]


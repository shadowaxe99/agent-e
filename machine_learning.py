```python
# machine_learning.py

# Import the necessary libraries for machine learning and AI
import nltk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Function to preprocess and tokenize the text data
def preprocess_text(text):
    # Tokenize the text into words
    tokens = nltk.word_tokenize(text)
    
    # Convert the words to lowercase
    tokens = [word.lower() for word in tokens]
    
    # Remove punctuation and special characters
    tokens = [word for word in tokens if word.isalnum()]
    
    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize the words
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

# Load the dataset for training the machine learning model
dataset = pd.read_csv('communication_history.csv')

# Preprocess the text data
dataset['tokens'] = dataset['text'].apply(preprocess_text)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(dataset['tokens'], dataset['label'], test_size=0.2, random_state=42)

# Convert the text data into numerical features using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Naive Bayes classifier on the vectorized training data
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Make predictions on the vectorized testing data
y_pred = classifier.predict(X_test_vectorized)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

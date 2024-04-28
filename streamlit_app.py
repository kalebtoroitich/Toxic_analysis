import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

# Function to preprocess the comment
def preprocess_comment(comment):
    # Add your preprocessing steps here if any
    return comment

# Function to predict toxicity
def predict_toxicity(comment):
    # Load your trained model here
    model = load_model("toxicity_model.h5")  

    # Tokenize and pad the comment
    # Add your tokenization and padding logic here based on how the model was trained
    # For example:
    # tokenized_comment = tokenizer.texts_to_sequences([comment])
    # padded_comment = pad_sequences(tokenized_comment, maxlen=max_length, padding='post')
    
    # Dummy prediction (replace with actual prediction)
    prediction = model.predict([[0]])  # Replace [[0]] with padded_comment
    
    return prediction

# Function to visualize comment length
def visualize_comment_length(comment):
    plt.figure(figsize=(8, 6))
    plt.hist([len(comment.split())], bins=30, color='skyblue')
    plt.title('Comment Length Distribution')
    plt.xlabel('Number of Words')
    plt.ylabel('Frequency')
    st.pyplot()

def main():
    # Title and description
    st.title("Toxic Comment Analysis")
    st.write("Welcome to the Toxic Comment Analysis App! Please enter your comment below and rate its toxicity.")

    # Comment input
    comment = st.text_area("Enter your comment", "")

    # Preprocess the comment
    preprocessed_comment = preprocess_comment(comment)

    # Toxicity rating
    toxicity_rating = st.select_slider("Rate the toxicity of the comment", options=[1, 2, 3, 4, 5])

    # Submit button
    if st.button("Submit"):
        # Predict toxicity
        prediction = predict_toxicity(preprocessed_comment)

        # Display predicted toxicity level
        st.write(f"Predicted Toxicity Level: {prediction}")

        # Visualize comment length
        visualize_comment_length(comment)

        # Provide feedback based on prediction
        if prediction > 0.5:
            st.error("Warning: This comment may contain toxic content.")
        else:
            st.success("This comment appears to be non-toxic.")

if __name__ == "__main__":
    main()

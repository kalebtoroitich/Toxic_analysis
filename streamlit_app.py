import streamlit as st
import matplotlib.pyplot as plt

def main():
    # Title and description
    st.title("Toxic Comment Analysis")
    st.write("Welcome to the Toxic Comment Analysis App! Please enter your comment below and rate its toxicity.")

    # Comment input
    comment = st.text_area("Enter your comment", "")

    # Toxicity rating
    toxicity_rating = st.select_slider("Rate the toxicity of the comment", options=[1, 2, 3, 4, 5])

    # Submit button
    if st.button("Submit"):
        # Display submitted comment and rating
        st.write("Submitted Comment:", comment)
        st.write("Toxicity Rating:", toxicity_rating)

if __name__ == "__main__":
    main()


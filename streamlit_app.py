import streamlit as st

def main():
    st.title("Comment Box")
    st.write("Please enter your comment below:")

    # Text input for the comment
    comment = st.text_area("Your Comment", "")

    # Button to submit the comment
    if st.button("Submit"):
        # Process the comment (you can add your processing logic here)
        process_comment(comment)
        st.success("Comment submitted successfully!")

def process_comment(comment):
    # Placeholder function for processing the comment
    # You can add your logic to process the comment here
    # For example, you can analyze sentiment, filter inappropriate content, etc.
    st.write("Processing comment:", comment)

if __name__ == "__main__":
    main()


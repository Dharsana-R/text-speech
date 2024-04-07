import streamlit as st
import pyttsx3

# Custom CSS style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to convert text to speech
def text_to_speech(text, rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    st.title("Text-to-Speech")

    # Load custom CSS
    local_css("styles.css")

    # Input text area
    st.write("")
    text_input = st.text_area("Enter Input Text")

    # Speech rate slider
    rate = st.slider("Select Speech Rate", min_value=100, max_value=300, step=10, value=200)

    # Convert to speech button
    if st.button("Convert to Speech"):
        if text_input:
            text_to_speech(text_input, rate)
            st.success("Speech generated successfully!")
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()

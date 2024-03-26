import speech_recognition as sr
import streamlit as st
import wave
from openai import OpenAI
import openai

openai.api_key = "your api key" 
client = openai.Client(api_key=openai.api_key)
def text_to_soap(text):
    """Generates a SOAP request string (extracted text)."""
    extracted_text = f"{text}"
    return extracted_text

def recognize_and_convert_to_soap(audio_file):
    """Recognizes speech from the uploaded audio file and creates a SOAP request."""
    r = sr.Recognizer()

    try:
        # Extract information from WAV file
        with wave.open(audio_file, "rb") as wave_file:
            sample_rate = wave_file.getframerate()
            sample_width = wave_file.getsampwidth()
            audio_data = audio_file.read()

        audio = sr.AudioData(audio_data, sample_rate=sample_rate, sample_width=sample_width)
        text_content = r.recognize_google(audio)
        print("Text from file:", text_content)

        # Summarize using OpenAI (optional)
        if openai.api_key is not None:  # Check if API key is provided
            prompt = "You have doctor and patient conversation text summarize text in soap format" + text_content
            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=150,  # Adjust max_tokens as needed
                n=1,
                stop=None,
                temperature=0.5,
            )
            summary = response.choices[0].text.strip()
            print("OpenAI Summary:", summary)
        else:
            summary = text_content  # Use full text if no OpenAI key

        soap_request = text_to_soap(summary)
        st.success("SOAP Request:")
        st.code(soap_request, language="xml")  # Display SOAP request in code block

    except sr.UnknownValueError:
        st.error("Could not understand audio")
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    """Streamlit app to handle audio upload, speech recognition, and SOAP conversion."""
    st.title("Speech to SOAP Converter")
    uploaded_file = st.file_uploader("Choose an audio file (WAV format)", type="wav")

    if uploaded_file is not None:
        recognize_and_convert_to_soap(uploaded_file)

if __name__ == "__main__":
    main()
# audio-to-soap-format

This Python code implements a web application that converts spoken audio files (WAV format) into SOAP requests. Here's a breakdown of its functionalities:

Speech Recognition:

It utilizes the speech_recognition library to recognize speech from uploaded audio files.
When a WAV file is uploaded, the code extracts audio data like sample rate and width.
It then converts the raw audio data into a format suitable for speech recognition using sr.AudioData.
Finally, it leverages Google Speech Recognition service (r.recognize_google) to convert the audio into text content.
Optional Summarization (using OpenAI):

The code checks if an OpenAI API key is provided. This key is necessary to access OpenAI's NLP capabilities.
If a key is available, it constructs a prompt that instructs the GPT-3.5-turbo-instruct model to summarize the recognized text content in SOAP format. This model is specifically designed for following instructions and generating different creative text formats.
OpenAI then returns a summarized version of the text in SOAP format.
SOAP Request Generation:

If no OpenAI key is provided, the code simply uses the full recognized text content.
Regardless of summarization, the code then utilizes the text_to_soap function (which can be further enhanced) to format the text (potentially summarized text) as a SOAP request string.
Web Application Interface (using Streamlit):

The code leverages the Streamlit framework to create a user-friendly web application.
It displays a title ("Speech to SOAP Converter") and provides a file upload option specifically for WAV audio files.
Once a file is uploaded, the code processes it through the functionalities mentioned above.
If successful, it displays a success message and presents the generated SOAP request in a code block formatted with the xml language for better readability.
In case of errors during speech recognition or Google Speech Recognition service issues, the code displays appropriate error messages using Streamlit's functionalities.
#### LLMs Used:

Google Speech Recognition: This service is used to convert the uploaded audio file's speech into text content. It's not technically an LLM (Large Language Model) but a powerful speech recognition tool.

OpenAI's GPT-3.5-turbo-instruct (Optional): This LLM is used conditionally, based on the presence of an OpenAI API key.  If the key is provided, the model  summarizes the recognized text content following the prompt's instruction to format it in SOAP format.

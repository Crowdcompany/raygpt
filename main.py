import streamlit as st
from litellm import completion
import json
import textwrap

st.title("RAYGPT")

# Function to get LLM response
def get_response(topic):
    response = completion(
        model="ollama/mistral-openorca",
        temperature=0,
        messages=[
            {"role": "system", "content": "Always answer in the language of the request. Always give short answers."},
            {"role": "user", "content": f"{topic}"},
        ],
        api_base="http://localhost:11434",
        stream=False
    )
    response_string = str(response)
    data = json.loads(response_string)
    message_content = data["choices"][0]["message"]["content"]
    return message_content

# Input from user
topic = st.text_input("Request / Anfrage:")

# Button to generate response
if st.button("Send / Senden"):
    st.write("Response / Antwort:")
    response = get_response(topic)
    st.write(response)

st.sidebar.markdown("Version 1 Alpha")
st.sidebar.text("Crowdcompany UG")

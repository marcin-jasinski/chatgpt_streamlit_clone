import streamlit as st
from openai import OpenAI

# Setup Streamlit app
st.title("ChatGPT Clone with LLama3")
st.caption("Locally hosted model with LM Studio")

# Initialize OpenAI Client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Chat history init
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# User input feed
if prompt := st.chat_input("What's up?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Get response from model
  response = client.chat.completions.create(
    model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
    messages=st.session_state.messages,
    temperature=0.7
  )

  # Show response in chat history
  st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
  with st.chat_message("assistant"):
      st.markdown(response.choices[0].message.content)

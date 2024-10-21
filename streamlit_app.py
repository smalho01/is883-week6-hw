import streamlit as st
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

# Show title and description.
st.title("💬 Chat GPT-2 Chatbot")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-2 model to generate text completion responses. "
)
token_length = st.number_input("Enter the number of tokens for this repsonse:", min_value=1, value=50)

# Ask for the user's input
if prompt := st.text_input("Enter your prompt for text completion:"):
    generator(prompt, max_length=token_length, num_return_sequences=10, truncation=True)



# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display the existing chat messages via `st.chat_message`.
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):

#     # Store and display the current prompt.
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)


    # # Generate a response using the OpenAI API.
    # stream = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": m["role"], "content": m["content"]}
    #         for m in st.session_state.messages
    #     ],
    #     stream=True,
    # )

    # # Stream the response to the chat using `st.write_stream`, then store it in 
    # # session state.
    # with st.chat_message("assistant"):
    #     response = st.write_stream(stream)
    # st.session_state.messages.append({"role": "assistant", "content": response})

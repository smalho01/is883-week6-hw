import streamlit as st
from transformers import GPT2LMHeadModel, AutoTokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

st.title("💬 Chat GPT-2 Completion Chatbot")
st.write("This is a simple chatbot that uses OpenAI's GPT-2 model to generate text completion responses.")

token_length = st.number_input("Enter the number of tokens for this repsonse:", min_value=1, value=50)
prompt = st.text_input("Enter your prompt for text completion:")

if st.button("Generate Response"):
    input = tokenizer.encode(prompt, return_tensors='pt')

    high_creativity_response = tokenizer.decode(model.generate(input, max_length=token_length, num_return_sequences=1, temperature=0.7, do_sample=True)[0])
    st.subheader("High Creativity Response:")
    st.write(high_creativity_response)

    low_creativity_response = tokenizer.decode(model.generate(input, max_length=token_length, num_return_sequences=1, temperature=0.3, do_sample=True)[0])
    st.subheader("Predictable Response:")
    st.write(low_creativity_response)
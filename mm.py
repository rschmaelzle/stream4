import streamlit as st 
from aitextgen import aitextgen 

st.title("MM")

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 
prompt_text = st.text_input(label = "Enter your prompt text...",
            value = "A horse walks into a bar.")

with st.spinner("AI is at Work........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 100 )
st.success("Successfully generated the below text ")
st.balloons()

# print generated text
print(gpt_text)

st.text(gpt_text)

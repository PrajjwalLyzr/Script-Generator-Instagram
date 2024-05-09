import streamlit as st
import os
from PIL import Image
from script_generator import script_generator, content_creator

# page config
st.set_page_config(
        page_title="Lyzr - Script Generator for Instagram",
        layout="centered",   
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

# style the app
st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app interface
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)
st.title('Script Generator for Instagram')
st.markdown('This app, the Script Generator for Instagram, will assist you in creating an appealing script for your Instagram video !!!')


api_key = st.sidebar.text_input('Enter OpenAI API Key', type='password')

user_input = st.text_area('Write a brief about your idea.')

example = st.sidebar.text_area('Input: Provide any example of a script you want. (Optional)',height=370)

if api_key:
    api_key = api_key.replace(" ","")
    if user_input:
        if st.button('Submit'):
            inital_script = script_generator(API_KEY=api_key,user_input=user_input, preference=example)
            generated_output = content_creator(script=inital_script, API_KEY=api_key)
            final_script = generated_output[0]['task_output']
            st.subheader('Script for your Instagram video')
            st.write(final_script)
           
    else:
        st.warning('Please provide a brief description of your script.')
else:
    st.sidebar.warning("Input: Enter your API key to proceed.")



with st.expander("ℹ️ - About this App"):
    st.markdown("This app utilizes Lyzr's Generator and Automata Agent to generate an appealing script for 60-second Instagram videos.")
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
    st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)





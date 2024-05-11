import streamlit as st
import os
from PIL import Image
import insta_script_generator

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


# Setting up the sidebar for input
st.sidebar.title("Instagram Script Generator")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type='password')
submit_api_key = st.sidebar.button("Submit API Key")
if submit_api_key:
    insta_script_generator.save_api_key(api_key)
    st.sidebar.success("API Key saved!")

# Navigation
page = st.sidebar.radio("Navigation", ["Add Examples", "Generate Script", "Edit Prompt"])

if page == "Add Examples":
    st.subheader('Add Your Example Text Here')
    col1, col2, col3 = st.columns(3)
    with col1:
        example_text1 = st.text_area("Example 1", height=400)
    with col2:
        example_text2 = st.text_area("Example 2", height=400)
    with col3:
        example_text3 = st.text_area("Example 3", height=400)

    submit_example = st.button("Submit Example")
    if submit_example:
        with open('examples.txt', 'r') as file:
            text = file.read()

        if text != '':
            with open('examples.txt', 'w') as file:
                pass

        insta_script_generator.save_example(example_text1)
        insta_script_generator.save_example(example_text2)
        insta_script_generator.save_example(example_text3)
        st.success("Example added!")

elif page == "Generate Script":
    instruction = st.text_input("Enter Your Instructions")
    submit_instruction = st.button("Generate Script")
    with open('examples.txt', 'r') as file:
        refrence = file.read()
    if submit_instruction:
        output = insta_script_generator.generate_script(instruction, refrence=refrence)
        st.subheader('Generated Script')
        st.write(output)
        # st.text_area("Generated Script", value=output, height=300)

elif page == "Edit Prompt":
    # Loading existing prompt if available
    if os.path.exists("prompt.txt"):
        with open("prompt.txt", "r") as file:
            existing_prompt = file.read()
    else:
        existing_prompt = ""
    prompt_text = st.text_area("Edit your prompt here:", value=existing_prompt, height=300)
    save_prompt_button = st.button("Save Prompt")
    if save_prompt_button:
        insta_script_generator.save_prompt(prompt_text)
        st.success("Prompt saved!")


with st.expander("ℹ️ - About this App"):
    st.markdown("This app utilizes Lyzr's Generator and Automata Agent to generate an appealing script for 60-second Instagram videos.")
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
    st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)





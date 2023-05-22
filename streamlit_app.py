from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

#Sidebar contents
with st.sidebar:
    st.title('⭐️ EinfachChat App ⭐️')
    
    # About section
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [Huggingface](https://huggingface.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    
    ''')
    
    # Image
    st.markdown('<img src="https://einfachalex.net/wp-content/uploads/2023/05/4-5.png" alt="Beschreibung des Bildes" width="200" style="float:left;">', unsafe_allow_html=True)
    
    # Made with love
    st.write('Made with ❤️💬 by [EinfachAlex](https://github.com/alfcodex)')

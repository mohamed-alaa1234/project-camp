# 1. Importing extensions
import streamlit as st

# 2. Creating app title
st.title('Welcome MECHATECH', 
         text_alignment='center')

# 3. App slogan
st.subheader('Best Electronics Store', 
            text_alignment='center')

# 4. Adding hero image
st.image("D:\WhatsApp Image 2026-04-22 at 12.32.48 AM.jpeg", use_container_width=True)
st.divider()

# 5. Creating columns
col1, col2 = st.columns(2, border=True)
with col1:
    st.header(' Shop Now!', text_alignment='center')
    st.subheader('Start exploring our menu')
    if st.button('Go to Menu ', 
                 use_container_width=True):
        st.switch_page('pages/menu.py')

with col2:
    st.header('✨ Need help?', text_alignment='center')
    st.subheader('Chat with our AI assitant')
    if st.button('Chat with AI ', 
                 use_container_width=True):
        st.switch_page('pages/chatbot.py')
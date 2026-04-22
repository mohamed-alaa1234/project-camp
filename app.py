# 1. Importing extensions
import streamlit as st

# 2. Converting files to pages
home_page = st.Page(
    page='pages/home.py',
    title='Home page',
    icon='🏠',
    default=True
)
signin_page = st.Page(
    page='pages/signin.py', 
    title='Sign In', 
    icon='🔑'
)
signup_page = st.Page(
    page='pages/signup.py', 
    title='Sign Up', 
    icon='📝'
)
menu_page = st.Page(
    page='pages/menu.py', 
    title='Components Store', 
    icon='🔌'
)
chatbot_page = st.Page(
    page='pages/chatbot.py', 
    title='Talk with AI', 
    icon='✨'
)

#3. creating navbar
all_pages = st.navigation(
    pages = [home_page, signin_page, signup_page, menu_page, chatbot_page]
    ,position = 'top'
    )
all_pages.run()
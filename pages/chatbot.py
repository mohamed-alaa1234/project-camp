# 1. Importing extensions
import streamlit as st
import google.generativeai as ai

# 2. Page title
st.title('Your AI Assistant is Here To Help You ✨', text_alignment='center')

# 3. Gemini API setup
key= 'AIzaSyAH6yg8w4IxFyvNzC-uyHxXXVJGXv3w228'
ai.configure(api_key=key)
# ملاحظة: تم تغيير اسم الموديل لـ gemini-1.5-flash لضمان عدم حدوث خطأ 404 كما ظهر لك سابقاً
model = ai.GenerativeModel(model_name='gemini-3.1-flash-lite-preview')

# 4. Taking user question
question = st.chat_input('Ask me anything..')

# 5. Creating chat messages & generating results
if question:
    with st.chat_message('human', avatar='👤'):
        st.write(question)
        
    # --- بداية الجزء المعدل (الرد والمعلومات) ---
    prompt = f'''
    Answer this question:
    {question}
    Use this knowledge to answer (You are an expert at MECHATECH store):
    - Working hours: 9AM to 11PM (Everyday)
    - Components & Pricing (EGP):
        * Arduino UNO: Small: 180, Medium: 250, Large: 320
        * Arduino MEGA: Small: 150, Medium: 210, Large: 270
        * Arduino NANO: Small: 200, Medium: 280, Large: 350
        * Jumper Wires: Male-Male (180), Male-Female (200), Female-Female (190)
        * Sensors: Ultrasonic (30), LDR (30), GAS (45), IR (15)
    
    Rule: Do not answer any question irrelevant to electronics or our components.
    '''
    # --- نهاية الجزء المعدل ---
    
    with st.chat_message('ai', avatar='✨'):
        with st.spinner('Generating...🧠'):
            answer = model.generate_content(prompt)
        st.write(answer.text)
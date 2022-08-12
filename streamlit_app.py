import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Dr. Milind Audichya, Ph.D. - Computer Science')
st.text('Helping people and businesses to grow more through technology')

st.text('Learner for Life, Educator, Researcher, Technocrat, Expert Freelancer')

icon_size = 25

st_button('linkedin', 'https://www.linkedin.com/in/drmkaudichya/', 'Follow me on LinkedIn', icon_size)
st_button('twitter', 'https://twitter.com/drmkaudichya/', 'Follow me on Twitter', icon_size)
st_button('facebook', 'https://www.facebook.com/drmkaudichya', 'Follow me on Facebook', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/drmkaudichya', 'Buy me a Coffee', icon_size)
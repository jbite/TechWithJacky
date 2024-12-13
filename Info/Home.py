import streamlit as st
import contents.inform as pInfo
st.title("Tech with Jacky")


col1, col2 = st.columns(2)
with col1:
    col3,col4 = st.columns([0.5,1])
    with col3:
        st.image("images/myphoto.jpg",width=150)
    with col4:
        st.markdown(f"""**Name**: Jacky Feng\n
**Phone**: {pInfo.PHONE}\n
**Email**: {pInfo.PERSONAL_EMAIL}""")

with col2:
    st.info("Hi, I am Jacky Feng, I am a associate consultant work in IT area over 10 years. ")

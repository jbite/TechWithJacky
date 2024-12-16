import streamlit as st
import contents.inform as pInfo
st.title("Tech with Jacky")


col1, col2 = st.columns(2)
with col1:
    st.image("images/myphoto.jpg", caption="Hi there",width=150)

with col2:
    st.write(f"""Github: {pInfo.GITHUB}\n
Email: {pInfo.PERSONAL_EMAIL}
             """)

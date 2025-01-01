import streamlit as st

st.set_page_config(page_title="Tech with Jacky", page_icon=":material/edit:",layout="wide")
home_page = st.Page("Info/Home.py", title="Home", icon=":material/home:",default=True)
aws_page = st.Page("My_Learning_Journey/AWS.py", title="AWS", icon=":material/cloud:")
python_page = st.Page("My_Learning_Journey/Python.py", title="Python", icon=":material/code:")
ml_page = st.Page("My_Learning_Journey/Machine_Learning.py", title="Machine Learning", icon=":material/robot_2:")
llm_page = st.Page("My_Learning_Journey\LLM_Engineering.py", title="LLM Engineernring", icon=":material/robot_3:")
videomesh_page = st.Page("Cisco_Collaboration/Video_mesh.py", title="Video Mesh", icon=":material/robot_2:")

pg = st.navigation(
    {   "Info": [home_page],
        "My Learning Journey": [aws_page, python_page,ml_page, videomesh_page,llm_page]
    }
)
pg.run()
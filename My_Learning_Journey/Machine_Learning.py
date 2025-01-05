import streamlit as st
from contents import LLM
Day1Title = "Try LLM"
Day1Content = """
- Try Ollama locally
- Complete a news summarize application with open API and reuqests
"""

Day2Title = "Compare to frontier"
Day2Content = """
- What are the frontiers of LLM model
  - OpenAI
  - Gemini
  - Cohere
  - Perplexity
- What can LLM model do?
  - synthesizeing information
  - fleshing out a skeleton 
  - coding
- Compare to those models
"""
st.title("LLM")
st.header(LLM.Day1Title)
st.write("**2025-01-01**")
st.write(LLM.Day1Content)


st.title(LLM.Day2Title)
st.write("**2025-01-02**")
st.write(LLM.Day2Content)

st.title(LLM.Day3Title)
st.write("**2025-01-03**")
st.write(LLM.Day3Content)

st.title(LLM.Day5Title)
st.write("**2025-01-05**")
st.write(LLM.Day5Content)
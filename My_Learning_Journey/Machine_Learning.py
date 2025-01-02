import streamlit as st

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
st.header(Day1Title)
st.write("**2025-01-01**")
st.write(Day1Content)


st.title("")
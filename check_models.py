import google.generativeai as genai
import os
import toml

secrets = toml.load(r"c:\Users\kjkyj\OneDrive\바탕 화면\2번째 프로젝트\.streamlit\secrets.toml")
genai.configure(api_key=secrets["GEMINI_API_KEY"])

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

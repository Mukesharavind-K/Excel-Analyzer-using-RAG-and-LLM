import google.generativeai as genai

genai.configure(api_key="AIzaSyCdufoLL72Uew6KtChbMyhOX3v5BqAETqI")  # Replace with your actual key

for m in genai.list_models():
    print(m.name)
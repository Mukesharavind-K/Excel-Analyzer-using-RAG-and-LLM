from flask import Flask, request, render_template
import google.generativeai as genai
import pandas as pd

app = Flask(__name__)

# ✅ Use your actual API key here
api_key = "AIzaSyCdufoLL72Uew6KtChbMyhOX3v5BqAETqI"
genai.configure(api_key=api_key)

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# ✅ Use a supported Gemini 2.5 model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-pro",
    generation_config=generation_config,
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        prompt = request.form["prompt"]

        df = pd.read_excel(file)
        data_str = df.to_string(index=False)

        try:
            # ✅ Use generate_content for single-turn prompt
            response = model.generate_content([data_str, prompt])
            result = response.text if response else "No response received from the API."
            return render_template("result.html", result=result)
        except Exception as e:
            return f"An error occurred: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

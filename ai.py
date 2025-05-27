# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

openai.api_key = 'your-openai-api-key'

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    # Replace this with your own prompt formatting if needed
    prompt = f"Based on the documentation, answer: {question}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant knowledgeable about the provided documentation."},
                  {"role": "user", "content": prompt}]
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({"answer": answer.strip()})

if __name__ == "__main__":
    app.run(debug=True)

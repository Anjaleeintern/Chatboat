from flask import Flask, request, jsonify, render_template
from simple_nlp_model import get_response  # Import your NLP processing function


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('message')
    response = get_response(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

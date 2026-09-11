from flask import Flask, render_template, request, jsonify
from main_agent import main_agent

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    reply, panel = main_agent(data["message"])

    response = {"reply": reply}

    if panel:
        response["panel"] = panel

    return jsonify(response)

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=5001)
from flask import Flask, request, jsonify
from ai_engine import generate_ai_reply
from affiliate_injector import add_affiliate_links

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask_ai():
    data = request.get_json()
    user_query = data.get("query")
    ai_reply = generate_ai_reply(user_query)
    reply_with_affiliates = add_affiliate_links(ai_reply)
    return jsonify({"response": reply_with_affiliates})

if __name__ == "__main__":
    app.run(debug=True)
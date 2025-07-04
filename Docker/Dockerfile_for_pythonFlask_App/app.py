from flask import Flask # type: ignore
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Welcome to Sk!</h1>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True,host='0.0.0.0',port=port)

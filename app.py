import os
from flask import Flask
from route.sample import sample

app = Flask(__name__)
app.register_blueprint(sample, url_prefix="/sample")

@app.route("/")
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':  # Running the app
    app.run(host="0.0.0.0", port=8000, debug=True)
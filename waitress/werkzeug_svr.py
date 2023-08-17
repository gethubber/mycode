#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Running a script with the werkzeug built in server"""
   
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'> Alta3 simple server! </h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Running a script with the waitress production server"""

from flask import Flask
# waitress must be imported to replace werkzeug
from waitress import serve


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'> Alta3 simple server! </h1>"

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=2224) # commented out
    # new serve() command is part of waitress
    # serve() syntax is here https://docs.pylonsproject.org/projects/waitress/en/latest/arguments.html#arguments
    serve(app, host='0.0.0.0', port=2224)


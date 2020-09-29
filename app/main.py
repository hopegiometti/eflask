from flask import Flask 
from flask import jsonify 
import json
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__) 
  
# @app.route("/") 
# def home_view(): 
#     return "<h1>Welcome to Geeks for Geeks</h1>"

spells = json.load(open("spells.json"))

app=Flask(__name__)
CORS(app)

@app.route('/')

def home():
    allspellnames = []

    for spell in spells:
        allspellnames.append(spell)
    
    return jsonify(allspellnames)

# def home():
#     return a


if __name__ == "__main__":
    app.run(debug=True)


#to run a flask app
#flask run 
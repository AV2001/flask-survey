from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'flask-survey-app'
app.config['DEBUG_TB_INTERCEPT_REDIRECTIONS'] = False
debug = DebugToolbarExtension(app)

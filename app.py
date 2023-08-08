from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)

# Setup flask debug toolbar
app.config['SECRET_KEY'] = 'flask-survey-app'
app.config['DEBUG_TB_INTERCEPT_REDIRECTIONS'] = False
debug = DebugToolbarExtension(app)

# List to keep track of user's responses
responses = []


# Root route that serves the home page
@app.route('/')
def home():
    title = surveys['satisfaction'].title
    instructions = surveys['satisfaction'].instructions
    return render_template('home.html', title=title, instructions=instructions)

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys, satisfaction_survey

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


@app.route('/questions/<int:id>')
def question_one(id):
    question = satisfaction_survey.questions[id].question
    choices = satisfaction_survey.questions[id].choices
    return render_template('questions.html', question=question, choices=choices)


@app.route('/answers', methods=['POST'])
def get_answers():
    answer = request.args.get('answer')
    responses.append(answer)
    if len(responses) == len(satisfaction_survey.questions):
        return render_template('thank-you.html')
    else:
        return redirect(f'/questions/{len(responses)}')

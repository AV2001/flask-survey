from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys, satisfaction_survey

app = Flask(__name__)

# Setup flask debug toolbar
app.config['SECRET_KEY'] = 'flask-survey-app'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


# Root route that serves the home page
@app.route('/')
def home():
    title = surveys['satisfaction'].title
    instructions = surveys['satisfaction'].instructions
    return render_template('home.html', title=title, instructions=instructions)


@app.route('/set-session', methods=['POST'])
def set_session():
    session['responses'] = []
    return redirect('/questions/0')


@app.route('/questions/<int:id>')
def question_one(id):
    questions = satisfaction_survey.questions
    if id == len(session['responses']):
        question = questions[id].question
        choices = satisfaction_survey.questions[id].choices
        return render_template('questions.html', question=question, choices=choices)
    elif len(session['responses']) == len(questions):
        return render_template('thank-you.html')
    flash(f'Sorry, you cannot visit this question as it is invalid!')
    return redirect(f'/questions/{len(session["responses"])}')


@app.route('/answers', methods=['POST'])
def get_answers():
    answer = request.form['answer']
    answers = session['responses']
    answers.append(answer)
    session['responses'] = answers
    if len(session['responses']) == len(satisfaction_survey.questions):
        return render_template('thank-you.html')
    else:
        return redirect(f'/questions/{len(session["responses"])}')

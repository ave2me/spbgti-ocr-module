from flask import Flask
app = Flask(__name__)

@app.run('0.0.0.0')


@app.route('/')
def index():
    return 'Here will be an index page'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<username>')
def greet_user(username):
    return 'Hello, {}!'.format(username)

@app.route('/ispalindrome/<string:word>')
def is_palindrome(word):
    if word[::-1] == word:
        return '{} is a palindrome.'.format(word)
    else:
        return 'No, {} isn\'t a palindrome'.format(word)
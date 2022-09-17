from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello world'
'''
@app.route('/bye')
def bye():
    return 'bye'
'''

def make_bold(function):
    def wrapper():
        return "<b>"+ function() +"</b>"
    return wrapper

def make_em(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>"+ function() +"</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_em
@make_underline
def bye():
    return "bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f'hello there {name}, you are {name} years old'

if __name__ == "__main__":
    app.run(debug=True)
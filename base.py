# from flask import Flask, render_template
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/report')
def report():
    # grab the inputs from the form, using request.
    username = request.args.get('username')
    return render_template("report.html", username=username)

    # Use regex to check for the constraints 
    x1 = re.search("[A-Z].+", username)
    x2 = re.search("[a-z].+", username)
    x3 = re.search("[0-9]$", username)

if __name__ == '__main__':
    app.run(debug=True)
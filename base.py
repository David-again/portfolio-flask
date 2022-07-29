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

    # Using Regex to check for the constraints: 
    lower_match_obj = re.search("[a-z]", username)
    upper_match_obj = re.search("[A-Z]", username)
    num_end_match_obj = re.search("[0-9]$", username)

    # Convert the RegEx Match objects into Booleans
    lower_letter = True if lower_match_obj else False
    upper_letter = True if upper_match_obj else False
    number_end = True if num_end_match_obj else False

    if lower_letter and upper_letter and number_end:
        all_true = True
    else:
        all_true = False

    # Here's what Jose used: 
    # lower_letter = any(c.islower() for c in username)

    return render_template("report.html", username=username, lower_passed=lower_letter, upper_passed=upper_letter, number_end_passed =number_end, all_true=all_true)

if __name__ == '__main__':
    app.run(debug=True)
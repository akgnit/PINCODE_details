from jinja2 import environment
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('entry.html', the_title='Pincode_data')

@app.route('/pincode', methods=['POST'])
def check_for_dnd():
    """
    Returns the postal index number code
    """
    pincode = request.form['NUMBER']
    host = "postalpincode.in"
    endpoint = "/api/pincode/"
    url = 'http://' + host + endpoint + pincode
    return render_template('results.html', result=json.loads(requests.get(url).content))

def check_type(var):
    if type(var) == list:
        return 'list'
    return type(var)

environment.DEFAULT_FILTERS['check_type'] = check_type

if __name__ == '__main__':
    app.run(debug=True)

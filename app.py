from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

data_file = 'form_data.json'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/onedown')
def onedown():
    return render_template('onedown.html')

@app.route('/oneup')
def oneup():
    return render_template('oneup.html')

@app.route('/partnership', methods=['GET', 'POST'])
def partnership():
    if request.method == 'POST':
        form_data = {
            'company_name': request.form['company_name'],
            'email': request.form['company_email'],
            'country': request.form['country'],
            'contribution': request.form['contribution'],
            'expectation': request.form['expectation'],
            'funding_costs': request.form['funding_costs']
        }

        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                data = json.load(f)
        else:
            data = []

        data.append(form_data)

        with open(data_file, 'w') as f:
            json.dump(data, f, indent=4)

        return redirect('/partnership')

    return render_template('partnership.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
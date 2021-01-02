from flask import Flask, render_template, redirect
from covid import grab_covid_stats, return_clean_covid_data
app = Flask(__name__)

@app.route('/')
def default_page():
    return redirect('/home')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/covid')
def covid_page():
    covid_data = return_clean_covid_data()
    return render_template('covid.html', tables=[covid_data.to_html(classes='data', index=False)], titles=covid_data.columns.values)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/test')
def test_function():
    return 'flask app v3'

if __name__ == '__main__':
    app.run(debug=False)
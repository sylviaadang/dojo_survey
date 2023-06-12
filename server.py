from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'happy'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/form_results')



@app.route('/form_results')
def show_results():
    return render_template('/results.html')



if __name__=="__main__":
    app.run(debug=True)

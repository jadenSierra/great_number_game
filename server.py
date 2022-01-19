from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def random_num():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/checker', methods=['POST'])
def guess_checker():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
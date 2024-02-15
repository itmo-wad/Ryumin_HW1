from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)

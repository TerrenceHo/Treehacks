from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "Test!"

@app.route('/federal/geographic')
def federal_geographic():
    pass

@app.route('/federal/issue')
def federal_issue():
    pass

@app.route('/state/geographic')
def state_geographic():
    pass

@app.route('/local/temporal')
def local_temporal():
    pass

if __name__ == "__main__":
    app.run(debug=True)

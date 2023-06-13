from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    wea={
        'weather': 'sun',
        'wind': 6,
        'wet': 15
    }
    return render_template('index.html',wea=wea)

if __name__ == '__main__':
    app.debug=True
    app.run(use_reloader=False)


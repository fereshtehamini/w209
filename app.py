from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def w209():
    file='visualization.vl.json'
    return render_template('w209.html',file=file)

if __name__ == '__main__':
    app.run()

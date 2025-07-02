from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def w209():
    file='AfricaPopulationMap_VLSpec.json'
    return render_template('index.html',file=file)

if __name__ == '__main__':
    app.run()

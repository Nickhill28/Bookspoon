from flask import Flask, render_template
from flask_assets import Bundle,Environment

app = Flask(__name__)

js = Bundle('app.js',output='gen/main.js')

assets = Environment(app)

assets.register('main_js',js)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=80)
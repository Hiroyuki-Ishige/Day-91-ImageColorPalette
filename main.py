from flask import Flask, render_template, redirect, url_for, flash, request, g
from flask_bootstrap import Bootstrap
from datetime import date, datetime, timedelta


app = Flask(__name__)
Bootstrap(app)

# Set up routes
@app.route('/')
def home():
    return render_template("index.html" )









if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


#TODO adjust navigation bar
#TODO to show photo
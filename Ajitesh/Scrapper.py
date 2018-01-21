
from flask import Flask, request, render_template, redirect
app = Flask(__name__)
host = 'http://localhost:5000/'




if __name__ == '__main__':

    table_check()
    app.run(debug=True)
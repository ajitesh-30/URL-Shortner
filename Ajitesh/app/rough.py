from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def validate():
	return render_template("index.html",show=tv_show)

if __name__ == "__main__":
	app.run()
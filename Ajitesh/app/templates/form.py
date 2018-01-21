from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
ef login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return request.form['username'];
        else:
            error = 'Invalid username/password'
 
    return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(debug=true);

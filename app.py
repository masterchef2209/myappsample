from flask import Flask,render_template,redirect,request,url_for,session
app=Flask(__name__)

@app.route('/')
def home():
	return 'Hello World!!!'

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():	
	error=None
	if request.method=='POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			error='Wrong Credentials. Access Denied!'
		else:
			session['logged_in']=True
			return redirect(url_for('home'))
	return render_template('login.html',error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in'.None)
	return redirect(url_for('welcome'))

if __name__=='__main__':
	app.run(debug=True)


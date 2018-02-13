from flask import Flask
from flask import render_template
from flask import request
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],
			       request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	# the code below is executed if the request method
	# was GET or the credentials were invalid
	return render_template('login.html', error=error)

with app.test_request_context('/hello', method='POST'):
	# now you can do something with the request until the
	# end of the with block, such as basic assertions:
	assert request.path == '/hello'
	assert request.method == 'POST'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

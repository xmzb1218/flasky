from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
#	user_agent = request.headers.get('User-Agent')
#	return '<p>You browser is %s!</p>' % user_agent
#	response = make_response('<h1>This document carries a cookie!<h1>')
#	response.set_cookie('answer', '42')
#	return response
	return redirect('http://www.example.com')
	
@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s!</h1>' % user.name
	
if __name__ == '__main__':
#	app.run(debug = True)
	manager.run()
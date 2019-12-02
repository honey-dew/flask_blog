from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
	{
		'author': 'Muhlis Adiwiguna',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2019'
	},

	{
		'author': 'Gugun',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 28, 2019'
	},

	{
		'author': 'Ade',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'May 2, 2019'
	}

]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About this website')

if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask
from datetime import datetime
from flask import render_template
#from pyblog import app

# creating the instance of Flask
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/home')
def home():

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/blog')
def blog():
    """Renders the blog page."""
    return render_template(
        'index.html',
    )

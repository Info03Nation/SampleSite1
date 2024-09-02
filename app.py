from flask import Flask, render_template, jsonify
app = Flask(__name__)

DATA = [
  {
    'id': 1,
    'Title': 'Python',
    'Description': 'Python is a high-level, general-purpose programming language.',
    'URL': 'https://www.python.org/'
  },
  {
    'id': 2,
    'Title': 'Flask',
    'Description': 'Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.',
    'URL': 'https://flask.palletsprojects.com/'
  },
  {
    'id': 3,
    'Title': 'Django',
    'Description': 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.',
    'URL': 'https://www.djangoproject.com/'
  },
  {
    'id': 4,
    'Title': 'FastAPI',
    'Description': 'FastAPI is a fast, asynchronous, high-performance web framework for building APIs with Python 3.6+.',
    'URL': 'https://fastapi.tiangolo.com/'
  },
  {
    'id': 5,
    'Title': 'HTML',
    'Description': 'Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. It defines the content and structure of web content. ',
    'URL': 'https://www.w3schools.com/html//'
  },
  {
    'id': 6,
    'Title': 'CSS',
    'Description': 'Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.' ,
    'URL': 'https://www.w3schools.com/css//'
  }
  
]

FORM =[
  {
  'id':1,
  'Name': '<name>'
  }
]

@app.route("/")
def hello_world():
  return render_template('Home.html', data = DATA)

@app.route("/")
def form_type():
  return render_template('Home.html', form = FORM)

@app.route("/api/data")
def list_content():
  return jsonify(DATA)  

@app.route("/api/data")
def form_content():
  return jsonify(FORM)  
# print(__name__)
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)

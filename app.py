from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

PROGRAMS = [
  {
    'id':1,
    'title':'Agribusiness',
    'years':'4 years',
    'location':'medford'
  },
  {
    'id':2,
    'title':'Accounting',
    'years':'4 years',
    'location':'remote'
  },
  {
  'id':3,
  'title':'Banking',
  'location':'medford'
  },
  {
  'id':4,
  'title':'General Business',
  'years':'3.5 years',
  'location':'remote'
  }
]
university_name = "University of Medford"

@app.route("/")
def hello_world():
  return render_template('home.html', programs=PROGRAMS, university_name=university_name)

@app.route("/api/programs")
def list_programs():
  return jsonify(PROGRAMS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
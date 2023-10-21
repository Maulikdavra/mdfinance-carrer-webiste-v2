from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000',
    'company': 'Google',
    'experiance': '2+ years'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New York',
    'salary': '$120,000',
    'company': 'NTT Data',
    'experiance': '3+ years'
  },
  {
    'id': 3,
    'title': 'Full Stack Developer',
    'location': 'Dallas',
    'salary': '$110,000',
    'company': 'State Farm',
    'experiance': '2+ years'
  },
  {
    'id': 4,
    'title': 'Associate developer',
    'location': 'Remote',
    'salary': '$90,000',
    'company': 'IBM',
    'experiance': '1+ years'
  },
]

@app.route("/")  
def hello():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


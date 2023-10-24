from flask import Flask, render_template, jsonify
from database import engine, text, load_job_from_db

app = Flask(__name__)


def load_jobs_from_db():
  try:
    with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      column_names = result.keys()
      jobs = []
      for row in result.all():
        jobs.append(dict(zip(column_names, row)))
    return jobs
  except Exception as e:
    print(f"An error occurred while loading jobs from database: {e}")
    return []


@app.route("/")
def hello():
  job_list = load_jobs_from_db()
  return render_template('home.html', jobs=job_list)


@app.route("/api/<id>")
def show_job(id):
  job_list = load_job_from_db(id)
  if not job_list:
    return "Not found", 404
  return render_template('jobpage.html', job=job_list)


@app.route("/api/jobs")
def list_jobs():
  job_list = load_jobs_from_db()
  return jsonify(job_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

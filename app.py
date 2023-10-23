from flask import Flask, render_template, jsonify
from database import engine, text

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


@app.route("/api/jobs")
def list_jobs():
  job_list = load_jobs_from_db()
  return jsonify(job_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

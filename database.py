from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())

# fetching data from mysql to replit by converting into python dictionaries
result_dict = []
for row in result.all():
  result_dict.append(dict(row))
print(result_dict)


def load_job_from_db(id):
  with engine.connect() as conn:
    query = text("select * from jobs where id = :val")
    result = conn.execute(query, {'val': id})
    rows = result.all()
    column_names = result.keys()

    if len(rows) == 0:
      return None
    else:
      # Using your suggested conversion technique
      return dict(zip(column_names, rows[0]))

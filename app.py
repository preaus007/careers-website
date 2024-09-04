from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "title": "Data Analyst",
    "company": "Tech Company",
    "location": "San Francisco, CA",
    "salary": "$100,000 - $120,000"
  },
  {
    "title": "Sodtware Engineer",
    "company": "Tech Company",
    "location": "San Francisco, CA",
    "salary": "$100,000 - $120,000"
  },
  {
    "title": "Marketing Head",
    "company": "Tech Company",
    "location": "San Francisco, CA",
    "salary": "$100,000 - $120,000"
  },
  {
    "title": "Cleaner",
    "company": "Tech Company",
    "location": "San Francisco, CA"
  }
]

@app.route('/')
def home():
  return render_template('index.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

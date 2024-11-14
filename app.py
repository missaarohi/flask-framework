from flask import Flask, json, render_template, jsonify

app = Flask(__name__)

JOBS = [
        {
            'id': 1,
            'title': 'Data Analyst',
            'Location': 'Bengaluru, India',
            'Salary': 'Rs.10,00,000'
        },
        {
            'id': 2,
            'title': 'Frontend Engineer',
            'Location': 'Delhi, India',
            'Salary': 'Rs.15,00,000'
        },
        {
            'id': 3,
            'title': 'Backend Engineer',
            'Location': 'Delhi, India',
            'Salary': 'Rs.12,00,000'
        },
        {
            'id': 4,
            'title': 'Data Scientist',
            'Location': 'San Francisco, USA',
            'Salary': '$120,000'
        }
    ]

@app.route("/")
def hello_tunes():
    return render_template('home.html', jobs=JOBS, company_name='Tune' )
    
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

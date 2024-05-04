from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

with open('job_data.json','r') as file :
    JOBS = json.load(file)

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='JobNexus')


@app.route('/apply/<int:job_id>')
def apply(job_id):
    job = next((job for job in JOBS if job['id'] == job_id), None)
    if job:
        return render_template('apply.html', job=job)
    else:
        return "Job not found", 404
    
@app.route('/',methods = ['GET','POST'])
def form_data():
    if request.method =='POST' : 

        full_name = request.form.get('full_name')
        email_address = request.form.get('email_address')
        phone_number = request.form.get('phone_number')
        customFile = request.form.get('customFile')

        print(full_name,email_address,phone_number,customFile)
    
    return render_template('apply')



if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from company_scrapper import fetch_jobs_wellfound,format_reponse
import random

app = Flask(__name__)

JOBS_BACKUP = [
    {
        "name": "Train Fitness",
        "title": "Senior Backend Engineer",
        "link": "https://wellfound.com/jobs/2954846-senior-backend-engineer"
    },
    {
        "name": "BigID",
        "title": "QA Automation Engineer",
        "link": "https://wellfound.com/jobs/2955114-qa-automation-engineer"
    },
    {
        "name": "CHA\u0398S AI Research Co.",
        "title": "Senior AI Researcher",
        "link": "https://wellfound.com/jobs/2955089-senior-ai-researcher"
    },
    {
        "name": "Collinear.ai",
        "title": "Sr. Machine Learning Engineer (LLM)",
        "link": "https://wellfound.com/jobs/2952888-sr-machine-learning-engineer-llm"
    },
    {
        "name": "Entrupy",
        "title": "Senior Full Stack Engineer(Knowledge)",
        "link": "https://wellfound.com/jobs/2955988-senior-full-stack-engineer-knowledge"
    },
    {
        "name": "AlphaSense",
        "title": "Senior Automation QA Engineer",
        "link": "https://wellfound.com/jobs/2955175-senior-automation-qa-engineer"
    },
    {
        "name": "Testlio",
        "title": "Sr Software Quality Engineer (XCUI, Espresso)",
        "link": "https://wellfound.com/jobs/2956187-sr-software-quality-engineer-xcui-espresso"
    },
    {
        "name": "SquaredLab",
        "title": "Senior Blockchain Dev (DeFi)",
        "link": "https://wellfound.com/jobs/2954815-senior-blockchain-dev-defi"
    },
    {
        "name": "AURA",
        "title": "DevOps Engineer",
        "link": "https://wellfound.com/jobs/2669366-devops-engineer"
    },
    {
        "name": "HashiCorp",
        "title": "Sr. Support Engineer, Vault",
        "link": "https://wellfound.com/jobs/2954052-sr-support-engineer-vault"
    },
    {
        "name": "ThoughtSpot",
        "title": "Senior Product Manager",
        "link": "https://wellfound.com/jobs/2946448-senior-product-manager"
    },
    {
        "name": "Fireflies.ai ",
        "title": "Senior Backend Engineer (Deep Learning team)",
        "link": "https://wellfound.com/jobs/2872929-senior-backend-engineer-deep-learning-team"
    },
    {
        "name": "Stripe",
        "title": "Software Engineer, RFA",
        "link": "https://wellfound.com/jobs/2952674-software-engineer-rfa"
    },
    {
        "name": "MongoDB",
        "title": "Manager, Technical Services",
        "link": "https://wellfound.com/jobs/2942901-manager-technical-services"
    },
    {
        "name": "6sense",
        "title": "Software Engineer II, Data",
        "link": "https://wellfound.com/jobs/2940779-software-engineer-ii-data"
    },
    {
        "name": "Zemoso Technologies",
        "title": "Node js Developer",
        "link": "https://wellfound.com/jobs/2956915-node-js-developer"
    },
    {
        "name": "Coupang",
        "title": "Staff System Engineer",
        "link": "https://wellfound.com/jobs/2956399-staff-system-engineer"
    },
    {
        "name": "Timescale",
        "title": "Database Support Engineer (Weekends)",
        "link": "https://wellfound.com/jobs/2947195-database-support-engineer-weekends"
    },
    {
        "name": "Icertis",
        "title": "Senior Software Engineer - Testing (Manual + Automation) - Data Science & AI",
        "link": "https://wellfound.com/jobs/2953013-senior-software-engineer-testing-manual-automation-data-science-ai"
    },
    {
        "name": "Autonomize",
        "title": "Senior MLOps Engineer",
        "link": "https://wellfound.com/jobs/2957077-senior-mlops-engineer"
    }
]

@app.route('/', methods=['GET', 'POST'])
def fetchJobs():
    if request.method == 'GET':
        location = request.args.get('location')
        if not location:
            return "No location provided"
        else:
            max_pages = 2
            job_list = []
            try : 
                for i in range(1, max_pages + 1):
                    job_data = fetch_jobs_wellfound(location, "", i)
                    if job_data : 
                        job_data = job_data
                    else : 
                        job_data = JOBS_BACKUP
                    jobs = format_reponse(job_data)
                    if not jobs:
                        break
                    job_list.append(jobs)
                
                for job in job_list : 
                    print(job)
                return job_list if job_list else JOBS_BACKUP

            except : 
                return JOBS_BACKUP
            
            

    return 'Hello World!'


if __name__ == '__main__':
    app.run()

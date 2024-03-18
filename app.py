from flask import Flask, request, jsonify
from company_scrapper import fetch_jobs

app = Flask(__name__)

JOBS_BACKUP = [
    {
        "Adyen": [
            {
                "link": "https://wellfound.com/jobs/2951408-team-lead-solution-engineering",
                "title": "Team Lead, Solution Engineering"
            }
        ],
        "Astranis": [
            {
                "link": "https://wellfound.com/jobs/2612927-senior-devops-engineer",
                "title": "Senior DevOps Engineer"
            }
        ],
        "Classy.org": [
            {
                "link": "https://wellfound.com/jobs/2956470-manager-software-engineering",
                "title": "Manager, Software Engineering"
            }
        ],
        "Feathery": [
            {
                "link": "https://wellfound.com/jobs/2886149-deployed-engineer",
                "title": "Deployed Engineer"
            }
        ],
        "HealthSherpa": [
            {
                "link": "https://wellfound.com/jobs/2956039-engineering-manager",
                "title": "Engineering Manager"
            }
        ],
        "Justworks": [
            {
                "link": "https://wellfound.com/jobs/2954566-senior-network-engineer",
                "title": "Senior Network Engineer "
            }
        ],
        "MongoDB": [
            {
                "link": "https://wellfound.com/jobs/2956299-senior-site-reliability-engineer",
                "title": "Senior Site Reliability Engineer"
            }
        ],
        "Nuna": [
            {
                "link": "https://wellfound.com/jobs/2954590-senior-software-engineer-ai",
                "title": "Senior Software Engineer, AI"
            }
        ],
        "Parafin": [
            {
                "link": "https://wellfound.com/jobs/2950719-staff-software-engineer-lending-products",
                "title": "Staff Software Engineer, Lending Products"
            }
        ],
        "Pendo": [
            {
                "link": "https://wellfound.com/jobs/2956426-front-end-engineer-guides",
                "title": "Front End Engineer: Guides"
            }
        ],
        "Qventus": [
            {
                "link": "https://wellfound.com/jobs/2950463-sr-data-platform-engineer",
                "title": "Sr. Data Platform Engineer"
            }
        ],
        "Roblox": [
            {
                "link": "https://wellfound.com/jobs/2955098-technical-director-generative-ai",
                "title": "Technical Director - Generative AI"
            }
        ],
        "SeatGeek": [
            {
                "link": "https://wellfound.com/jobs/2954887-lead-product-manager-cloud-and-data-products",
                "title": "Lead Product Manager - Cloud and Data Products"
            }
        ],
        "Snapdocs": [
            {
                "link": "https://wellfound.com/jobs/2950303-staff-security-engineer",
                "title": "Staff Security Engineer"
            }
        ],
        "Tanium": [
            {
                "link": "https://wellfound.com/jobs/2940074-servicenow-technical-architect",
                "title": "ServiceNow Technical Architect"
            }
        ],
        "Thumbtack": [
            {
                "link": "https://wellfound.com/jobs/2954938-lead-data-scientist-product",
                "title": "Lead Data Scientist, Product"
            }
        ],
        "Train Fitness": [
            {
                "link": "https://wellfound.com/jobs/2954846-senior-backend-engineer",
                "title": "Senior Backend Engineer"
            }
        ],
        "Up&Up": [
            {
                "link": "https://wellfound.com/jobs/2955646-technical-product-manager",
                "title": "Technical Product Manager"
            }
        ],
        "Wunderkind (formerly BounceX)": [
            {
                "link": "https://wellfound.com/jobs/2954557-senior-business-development-director-strategic",
                "title": "Senior Business Development Director, Strategic"
            }
        ],
        "Wynd Labs": [
            {
                "link": "https://wellfound.com/jobs/2956859-embedded-systems-engineer",
                "title": "Embedded Systems Engineer"
            }
        ]
    },
    {
        "Arcade": [
            {
                "link": "https://wellfound.com/jobs/2878172-engineering-manager",
                "title": "Engineering Manager"
            }
        ],
        "Arena ": [
            {
                "link": "https://wellfound.com/jobs/684391-machine-learning-scientist",
                "title": "Machine Learning Scientist"
            }
        ],
        "Bezi": [
            {
                "link": "https://wellfound.com/jobs/2849415-software-engineer-backend-security",
                "title": "Software Engineer (Backend, Security)"
            }
        ],
        "Classy.org": [
            {
                "link": "https://wellfound.com/jobs/2956470-manager-software-engineering",
                "title": "Manager, Software Engineering"
            }
        ],
        "Cruise": [
            {
                "link": "https://wellfound.com/jobs/2956503-senior-python-build-engineer-ii-build-platform",
                "title": "Senior Python Build Engineer II, Build Platform"
            }
        ],
        "Faire": [
            {
                "link": "https://wellfound.com/jobs/2846195-data-scientist-search-recommendation-machine-learning",
                "title": "Data Scientist - Search & Recommendation, Machine Learning "
            }
        ],
        "Fictiv": [
            {
                "link": "https://wellfound.com/jobs/2945036-supplier-quality-engineer",
                "title": "Supplier Quality Engineer"
            }
        ],
        "HubSpot": [
            {
                "link": "https://wellfound.com/jobs/2956289-technical-lead-frontend-crm",
                "title": "Technical Lead, Frontend, CRM "
            }
        ],
        "Instabase": [
            {
                "link": "https://wellfound.com/jobs/2937862-forward-deployed-solutions-engineer-federal",
                "title": "Forward Deployed Solutions Engineer (Federal)"
            }
        ],
        "Justworks": [
            {
                "link": "https://wellfound.com/jobs/2954566-senior-network-engineer",
                "title": "Senior Network Engineer "
            }
        ],
        "Notion": [
            {
                "link": "https://wellfound.com/jobs/2665332-software-engineer-web-performance",
                "title": "Software Engineer, Web Performance"
            }
        ],
        "Photon Health": [
            {
                "link": "https://wellfound.com/jobs/2953396-software-engineer",
                "title": "Software Engineer"
            }
        ],
        "RapidSOS": [
            {
                "link": "https://wellfound.com/jobs/2951300-business-development-partnership-manager",
                "title": "Business Development & Partnership Manager"
            }
        ],
        "Ripple": [
            {
                "link": "https://wellfound.com/jobs/2952581-senior-software-engineer-data-liquidity",
                "title": "Senior Software Engineer, Data (Liquidity)"
            }
        ],
        "Skydio": [
            {
                "link": "https://wellfound.com/jobs/2953155-flight-test-engineer",
                "title": "Flight Test Engineer"
            }
        ],
        "Snapdocs": [
            {
                "link": "https://wellfound.com/jobs/2950303-staff-security-engineer",
                "title": "Staff Security Engineer"
            }
        ],
        "Tanium": [
            {
                "link": "https://wellfound.com/jobs/2940074-servicenow-technical-architect",
                "title": "ServiceNow Technical Architect"
            }
        ],
        "Up&Up": [
            {
                "link": "https://wellfound.com/jobs/2955646-technical-product-manager",
                "title": "Technical Product Manager"
            }
        ],
        "UseBump.com": [
            {
                "link": "https://wellfound.com/jobs/2843732-vp-of-engineering",
                "title": "VP of Engineering"
            }
        ],
        "Volt Labs": [
            {
                "link": "https://wellfound.com/jobs/2855754-product-software-engineer",
                "title": "Product & Software Engineer"
            }
        ]
    }
]


@app.route('/', methods=['GET', 'POST'])
def fetchJobs():
    if request.method == 'POST':
        location = request.args.get('location')
        if not location:
            return "No location provided"
        else:
            max_pages = 2
            job_list = []
            for i in range(1, max_pages + 1):
                jobs = fetch_jobs(location, "", i)
                if not jobs:
                    break
                job_list.append(jobs)

            return jsonify(job_list) if job_list else JOBS_BACKUP

    return 'Hello World!'


if __name__ == '__main__':
    app.run()

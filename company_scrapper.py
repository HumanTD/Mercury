import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import pprint

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
HEADERS = ({"User-Agent": user_agent, "Content-Encoding": "br", "Cf-Ray": "865efb10dc77f3a5-BOM",
            "Cookie": "ajs_anonymous_id=63153436-7aaf-4b38-ba88-43580c577f8d; _wellfound=aa63168ca1d3975fa811dd3d4d9d71e5; _gcl_au=1.1.1858267607.1710694766; _hjSession_1444722=eyJpZCI6ImZmMzVjNGI0LTEzOGEtNDVmMy1hMDE4LWViNGJiMjZiZDM4MyIsImMiOjE3MTA2OTQ3NjU1NTcsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxfQ==; _fbp=fb.1.1710694765588.9572783; _hjSessionUser_1444722=eyJpZCI6ImJjYjBhYjNkLWE1YzgtNTA5ZC05NGNmLWE1Y2I4MGQ4NjJjMCIsImNyZWF0ZWQiOjE3MTA2OTQ3NjU1NTcsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.661819419.1710694766; datadome=g_PKAobcHT6hxUQ91f7M0Rgb5v76GTj8s26TQ3AUr0C61YPjD40KiZr7fMC4Ra~B_tCqLAKNBKcZl04Q97d6wHKxJBE4iSo_3eLlFm8ADvQB8cygqD_EpeGR9DP2Ffiy; _ga_705F94181H=GS1.1.1710698960.2.1.1710698997.23.0.0"})


def fetch_jobs_wellfound(location, role, page):
    jobs = []
    if page == 0:
        URL = f'''https://wellfound.com/location/{location}'''
    else:
        URL = f'''https://wellfound.com/location/{location}?page={page}'''
    print(URL)
    doc = requests.get(URL)
    role = ""
    location = "united-states"
    if not doc:
        print("Error fetching URL")
        return None
    soup = BeautifulSoup(doc.content, 'html.parser')

    jobs_dict = {}

    job_listings = soup.findAll('div', class_='styles_result__rPRNG')
    # inside the job listings div loop through all the a tags to get job title and link
    for job in job_listings:
        company_name = job.find('h4', class_='styles_name__rSxBl').text
        job_title = job.find('a', class_='styles_jobTitle___jT4l').text
        job_link = job.find('a', class_='styles_jobTitle___jT4l')['href']
        upd_job_link = f'''https://wellfound.com{job_link}'''
        #  in the jobs_dict match the company name to an array of job titles and links

        # print(type('https://wellfound.com'), type(job_link))
        if company_name in jobs_dict:
            jobs_dict[company_name].append(
                {'title': job_title, 'link': upd_job_link})
        else:
            jobs_dict[company_name] = [
                {'title': job_title, 'link': upd_job_link}]

    pprint.pprint(jobs_dict)
    return jobs_dict


def fetch_jobs_ycombinator():
    jobs = []
    URL = "https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&sortBy=created_desc&tab=any&usVisaNotRequired=any"

    post_response = requests.post(url_post, json=new_data)

    # Print the response
    post_response_json = post_response.json()
    print(post_response_json)


def format_reponse(job_data):
    # Convert JSON string to Python dictionary
    # Initialize an empty list to store the formatted data
    formatted_data = []

    # Loop through each company and its job listings
    for company, jobs in job_data[0].items():
        for job in jobs:
            formatted_data.append(
                {"name": company,
                 "title": job["title"],
                 "link": job["link"]}
            )

    # Convert the formatted data list back to JSON format
    formatted_json = json.dumps(formatted_data, indent=4)

    # Print the formatted JSON data
    print(formatted_json)


if __name__ == "__main__":
    location = "china"

    max_pages = 10
    job_list = []
    for i in range(1, max_pages + 1):
        jobs = fetch_jobs_wellfound(location, "", i)
        if not jobs:
            break
        job_list.append(jobs)

    print(job_list)

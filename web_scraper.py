import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_jobs():
    try:
        url = "https://vacancymail.co.zw/jobs/"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes

        soup = BeautifulSoup(response.content, "html.parser")
        job_cards = soup.select("div.job-summary")[:10]  # top 10 jobs

        jobs = []
        for card in job_cards:
            title = card.select_one("a.job-title").text.strip()
            company = card.select_one("div.company").text.strip()
            location = card.select_one("div.location").text.strip()
            expiry = card.select_one("div.expiry-date").text.strip()
            desc = card.select_one("div.job-description").text.strip()

            jobs.append({
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Expiry Date": expiry,
                "Description": desc
            })

        df = pd.DataFrame(jobs)
        df.drop_duplicates(inplace=True)
        df.to_csv("scraped_data.csv", index=False)

        logging.info("Successfully scraped and saved job data.")

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")

# Schedule it every hour
schedule.every(1).hours.do(scrape_jobs)

# Run once at script start
scrape_jobs()

# Keep it running
while True:
    schedule.run_pending()
    time.sleep(60)

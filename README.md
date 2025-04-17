# 💼 Job Scraper & Data Aggregator

This project is a Python-based web scraper that extracts job listings from [vacancymail.co.zw/jobs](https://vacancymail.co.zw/jobs/), stores them in a CSV file, and automates the process with optional scheduling.

---

## 🚀 Features

- 🔎 Scrapes the 10 most recent job listings
- 📍 Extracts: Job Title, Company, Location, Expiry Date, and Description
- 💾 Saves data to `scraped_data.csv`
- 🔁 Automates scraping every hour (or set your own interval)
- 📓 Logs key events and errors in `scraper.log`
- ✅ Uses modern Python libraries like `requests`, `BeautifulSoup`, `pandas`, and `schedule`

---

## 📦 Requirements

Install dependencies with pip:

```bash
pip install -r requirements.txt

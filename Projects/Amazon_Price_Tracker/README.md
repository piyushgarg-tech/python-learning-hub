# Amazon Price Tracker

## Overview

Amazon Price Tracker is a Python-based web scraping and automation project that monitors product prices from Amazon, stores historical pricing data, downloads product images, and compares current prices against user-defined target prices.

The project demonstrates practical use of web scraping, data collection, file handling, automation, and object-oriented programming concepts using Python.

---

## Features

* Track multiple Amazon products simultaneously
* Extract product titles and current prices
* Compare prices against custom target values
* Store historical price records in CSV format
* Download and save product images automatically
* Record timestamps for each price check
* Handle network and request errors gracefully
* Organize collected data for future analysis

---

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* lxml
* CSV
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
WebScraping/
├── README.md
├── requirements.txt
├── price_tracker.py
├── data/
│   ├── prices.csv
│   └── product_images/
├── screenshots/
└── demo/
```

---

## How It Works

1. Fetches product pages from Amazon.
2. Extracts product information including title and price.
3. Compares the current price with a predefined target price.
4. Stores product data and timestamps in a CSV file.
5. Downloads and saves product images locally.
6. Displays a recommendation based on the target price.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd WebScraping
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python price_tracker.py
```

---

## Skills Demonstrated

This project demonstrates practical experience with:

* Web Scraping
* HTTP Requests and Response Handling
* HTML Parsing
* Data Collection and Storage
* File Handling
* Error Handling
* Automation
* Object-Oriented Programming
* Working with Real-World Data

---

## Sample Output

```text
Product: Samsung Galaxy S25
Checked at: 14:32:10 10-06-2026
Price: 74999

BUY NOW! Price 74999 is below your target 100000

Data and Image saved!
```

---

## Future Improvements

* Email notifications for price drops
* Scheduled automatic price monitoring
* Support for additional e-commerce websites
* Data visualization and price trend analysis
* Configuration through JSON files

---

## Author

Piyush

BS Degree in Data Science – IIT Madras

Building skills in Python, Data Science, Web Development, and DevOps through hands-on projects and continuous learning.

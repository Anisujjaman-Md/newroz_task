# Inspirational Quotes Scraper

This Python script scrapes inspirational quotes from a website and saves them to a CSV file.

## Requirements

- Python 3.8+

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Anisujjaman-Md/newroz_task.git

   ```

2. Navigate to the project directory:

   ```shell
   cd newroz_task/scripts # for Linux/Mac

   ```

3. Create a virtual environment and activate it:

   ```shell
   python3 -m venv venv
   source venv/bin/activate  # for Linux/Mac
   venv\Scripts\activate  # for Windows

   ```

4. Install the dependencies:

   ```shell
   pip install -r requirements.txt

   ```

5. Run the script:

   ```shell
    python bq_sraping.py

   ```

# Explanation

The script randomly selects a user-agent string to mimic a real browser and then sends an HTTP request to the BrainyQuote website to retrieve the HTML content. It uses BeautifulSoup to parse the HTML and extract the desired data, which includes the quote and author information. The scraped data is then written to a CSV file.

# File Structure

bq_sraping.py: The main Python script for scraping quotes.
inspirational_quotes.csv: The output CSV file where the scraped quotes are stored.

# Note

- If the CSV file inspirational_quotes.csv already exists in the project directory, the script will skip the scraping process to prevent duplicate data.

- If the script encounters a HTTP 403 error, try running the script again.

import requests
from bs4 import BeautifulSoup
import csv
import random
import os


# List of common User-Agent strings
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.41',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.254'
]

# Randomly select a User-Agent string
random_user_agent = random.choice(user_agents)

# Headers to mimic a real browser
headers = {
    'User-Agent': random_user_agent
}


def scrape_quotes():
    try:
    # URL to scrape
        url = 'https://www.brainyquote.com/topics/inspirational-quotes'
        
        response = requests.get(url, headers=headers)
        print(response)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all quote elements on the page
            table_rows = soup.find_all('div', class_='grid-item')

            # Open a CSV file to write the scraped data
            with open('../project/inspirational_quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header row to the CSV file
                writer.writerow(['Quote', 'Author'])

                for row in table_rows:
                    # Find quote and author tags within the quote element
                    quote_tag = row.find('a', class_='b-qt')
                    author_tag = row.find('a', class_='bq-aut')
                    
                    
                    if quote_tag and author_tag:
                        # Extract text content of the quote and author
                        quote = quote_tag.text.strip()
                        author = author_tag.text.strip()
                        
                        print(f"Quote: {quote}\nAuthor: {author}\n")
                        
                        # Write the quote and author to the CSV file
                        writer.writerow([quote, author])
                    else:
                        print("Quote or author not found in this row.")
        
    except requests.RequestException as e:
        print("Error fetching web page:", e)
    except Exception as e:
        print("An error occurred:", e)


def main():
    # Check if the CSV file already exists
    if os.path.exists('../project/inspirational_quotes.csv'):
        print("CSV file already exists. Skipping scraping process.")
    else:
        # Continue with the scraping process
        scrape_quotes()

if __name__ == "__main__":
    main()
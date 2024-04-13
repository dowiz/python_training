import requests
from bs4 import BeautifulSoup

# Function to scrape exchange rates from a given URL


def scrape_exchange_rates(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # # Write your code here to extract the exchange rates from the HTML content

    # # Return the extracted exchange rates
    # return exchange_rates


# Scrape exchange rates from PrivatBank
privatbank_url = 'https://www.privatbank.ua/'
privatbank_rates = scrape_exchange_rates(privatbank_url)

# Scrape exchange rates from Monobank
monobank_url = 'https://www.monobank.ua/'
monobank_rates = scrape_exchange_rates(monobank_url)

# Scrape exchange rates from National Bank
nationalbank_url = 'https://www.bank.gov.ua/'
nationalbank_rates = scrape_exchange_rates(nationalbank_url)

# Scrape exchange rates from Ministry of Finance
minfin_url = 'https://www.minfin.gov.ua/'
minfin_rates = scrape_exchange_rates(minfin_url)

# Print the exchange rates
print('PrivatBank:', privatbank_rates)
print('Monobank:', monobank_rates)
print('National Bank:', nationalbank_rates)
print('Ministry of Finance:', minfin_rates)

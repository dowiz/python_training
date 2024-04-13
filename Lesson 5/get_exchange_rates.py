import requests
import json
from pprint import pprint as pp


privatbank_rates_cash = requests.get(
    'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()
privatbank_rates_non_cash = requests.get(
    'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11').json()

# dictionary_of_requests = {
#     'privatbank': [privatbank_rates_cash, privatbank_rates_non_cash],
#     'monobank': 'https://api.monobank.ua/bank/currency',
#     'nationalbank': 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
# }

answers_to_requests = [{
    'privatbank': {
        'cash': {
            rate['ccy']: {
                'buy': rate['buy'],
                'sale': rate['sale']
            } for rate in privatbank_rates_cash
        },
        'non_cash': {
            rate['ccy']: {
                'buy': rate['buy'],
                'sale': rate['sale']
            } for rate in privatbank_rates_non_cash
        }
    }
}]

exchange_rates = [{
    'bank': 'PrivatBank',
    'type': type,
    'ccy': rate,
    'rate': request['privatbank'][type][rate]
} for request in answers_to_requests
    for type in request['privatbank']
    for rate in request['privatbank'][type]
]


#     'cash': {
#         rate['ccy']: {
#             'buy': rate['buy'],
#             'sale': rate['sale']
#         } for rate in privatbank_rates_cash
#     },
#     'non_cash': {
#         rate['ccy']: {
#             'buy': rate['buy'],
#             'sale': rate['sale']
#         } for rate in privatbank_rates_non_cash
#     }
# }]

# Save the results in JSON format
with open('exchange_rates.json', 'w') as file:
    json.dump(exchange_rates, file, indent=4)

# Load the results from the JSON file
with open('exchange_rates.json', 'r') as file:
    exchange_rates = json.load(file)

pp(exchange_rates)

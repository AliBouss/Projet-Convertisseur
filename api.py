from datetime import date, datetime, timedelta
from pprint import pprint

import requests


def get_rates(devis, days=30):
    """Fonction qui permet de récuperer nos devises"""

    end_date = date.today()  # date aujordhui
    start_date = end_date - timedelta(days=days)  # date de la fin

    symbols = ','.join(devis)  # parametre devis qui doit recevoir une liste de devis separer par des virgules

    r = requests.get(f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}")

    if not r and not r.json:
        return False, False

    api_rates = r.json().get("rates")

    all_rates = {devi: [] for devi in devis}

    all_days = sorted(api_rates.keys())

    for each_day in all_days:
        [all_rates[devi].append(rate) for devi, rate in api_rates[each_day].items()]

    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(devis=["USD", "CAD"])
    pprint(days)
    pprint(rates)





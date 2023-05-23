import pandas as pd
import matplotlib.pyplot as plt


def build_plot():
    data_link = pd.read_json(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&sort=exchangedate&order=asc&json')
    data = pd.DataFrame({"date": data_link[data_link['cc'] == "USD"]['exchangedate'].values,
                          'USD': data_link[data_link['cc'] == "USD"]['rate'].values,
                          'EUR': data_link[data_link['cc'] == "EUR"]['rate'].values})
    data.to_csv("data.csv", index=False)
    data.plot(x='date', y=['USD', 'EUR'], figsize=(20, 10), title="UAH exchange rate")
    plt.savefig('plot.png')


build_plot()
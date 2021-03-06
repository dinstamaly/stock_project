import requests
import re
from io import StringIO
import time
import pandas as pd


def get_yahoo_ticker_data(ticker):
    res = requests.get(
        'https://finance.yahoo.com/quote/' + ticker + '/history'
    )
    yahoo_cookie = res.cookies['B']
    yahoo_crumb = None
    pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')
    for line in res.text.splitlines():
        m = pattern.match(line)
        if m is not None:
            yahoo_crumb = m.groupdict()['crumb']
    cookie_tuple = yahoo_cookie, yahoo_crumb

    current_date = int(time.time())
    url_kwargs = {'symbol': ticker, 'timestamp_end': current_date,
        'crumb': cookie_tuple[1]}
    url_price = 'https://query1.finance.yahoo.com/v7/finance/download/' \
                '{symbol}?period1=0&period2={timestamp_end}&interval=1d&events=history' \
                '&crumb={crumb}'.format(**url_kwargs)

    response = requests.get(url_price, cookies={'B': cookie_tuple[0]})
    if response:
        return pd.read_csv(StringIO(response.text), parse_dates=['Date'])
    else:
        return None

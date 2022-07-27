import cfg
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime


def get_crypto_data(API_KEY):
    """
    Get raw data in json format from Coinmarketcap API

    Parameters
    ----------
    API_KEY : str
        It's a API KEY to authenticate with Coinmarketcap API

    Returns
    -------
    dict
        Raw data of the All cryptocurrency of the Coinmarketcap.
    """

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'50',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
  


def extract():
    """
    Returns
    -------
    dict
        Raw data of the All cryptocurrency of the Coinmarketcap.
    """
    data_raw = None  

    for API_KEY in cfg.API_KEYS:
        data_raw = get_crypto_data(API_KEY)
        if data_raw != None: 
            break
    return data_raw

def main():
    """
    The main function runs the program.
    """
    # extract
    print(cfg.API_KEYS)
    data_raw = extract()
    curr = str(datetime.now().strftime("%Y-%m-%d_%H:%M"))

    with open(f"crypto-data/{curr}.json",'w+') as f:
        f.write(json.dumps(data_raw, indent=4, sort_keys=True))
    
    #transform
def ahhhh():
    print(f"AHHHHHHHHHHH {datetime.now()} AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

    # load
if __name__ == '__main__':
    main()


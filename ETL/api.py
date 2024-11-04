import requests
import pandas as pd
import os 


def get_request(url, params=None):
    response = requests.get(url, params=params)
    return response.json()['data'] if response.ok and len(response.json()['data'])>0 else None

def json_to_csv(date, json_data):
    df = pd.DataFrame(json_data)
    df = df.iloc[:, 1:]
    df.to_csv(f'output_{date}.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    date = '20241101'
    df = pd.read_csv('whsal.csv')
    df = df.to_dict(orient='records')
    result = []
    for i in range(0,len(df)):
        codeId = df[i]['codeId']
        url = "https://at.agromarket.kr/openApi/price/sale.do"
        params = {
        'serviceKey': os.getenv('API_SERVICE_KEY') ,
        'apiType': 'json',
        'pageNo': 1,
        'whsalCd': codeId,
        'saleDate': date
        }
        data = get_request(url, params=params)
        if data:
            result += data
    json_to_csv(date, result)
    

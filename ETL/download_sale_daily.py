import requests
import pandas as pd
import os 
import sys


def get_request(url, params=None):
    response = requests.get(url, params=params)
    return response.json()['data'] if response.ok and len(response.json()['data'])>0 else None

def json_to_csv(date, json_data):
    df = pd.DataFrame(json_data)
    df = df.iloc[:, 1:]
    df.to_csv(f'output_{date}.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("PARAMETER ERROR : python [filename] [yearmonthday]\n ex) python download_and_S3_put.py 20240307 ")
    elif len(sys.argv) > 3:
        print("PARAMETER ERROR : python [filename] [yearmonthday]\n ex) python download_and_S3_put.py 20240307 ")
    elif len(sys.argv[1]) != 8:
        print("년(4자리)월(2자리)일(2자리) 총 8자리 숫자가 인자로 입력되어야 합니다.")
    else:
        date = sys.argv[1]
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
    

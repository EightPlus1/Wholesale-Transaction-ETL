import requests
import pandas as pd
import os 
import sys
import boto3
from botocore.exceptions import NoCredentialsError

# AWS S3에 접근하기 위한 자격 증명 설정
ACCESS_KEY = os.getenv('S3_ACCESS_KEY')  
SECRET_KEY = os.getenv('S3_SECRET_KEY')  



def get_request(url, params=None):
    response = requests.get(url, params=params)
    return response.json()['data'] if response.ok and len(response.json()['data'])>0 else None

def json_to_csv(date, json_data):
    df = pd.DataFrame(json_data)
    df = df.iloc[:, 1:]
    df.to_csv(f'{date}.csv', index=False, encoding='utf-8')
    return f'{date}.csv'

def upload_to_s3(file_name, bucket, object_name=None):
    # S3 클라이언트 생성
    s3_client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

    # 파일 업로드
    if object_name is None:
        object_name = file_name  # S3에 저장될 파일 이름 지정
    
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"'{file_name}' -> '{bucket}/{object_name}' 업로드 완료")
    except FileNotFoundError:
        print(f"'{file_name}' 미존재")
    except NoCredentialsError:
        print("권한 미허용.")
    except Exception as e:
        print(f"Error: {e}")

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
        # 데이터 수집
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
        
        # 수집된 json을 csv파일로 변환
        file_name = json_to_csv(date, result)

        # csv파일을 S3로 적재
        bucket_name = 'sunjae-test-bucket'   # S3 버킷 이름
        object_name = f'project/{file_name}' # S3에 저장될 파일 경로 및 이름 (옵션)
        upload_to_s3(file_name, bucket_name, object_name)
    

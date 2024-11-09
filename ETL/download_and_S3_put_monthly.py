import requests
import boto3
import os
import sys

# AWS S3에 접근하기 위한 자격 증명 설정
ACCESS_KEY = os.getenv('S3_ACCESS_KEY')  # 환경변수 값
SECRET_KEY = os.getenv('S3_SECRET_KEY')  # 환경변수 값


# 파일 id 찾는 함수
def find_file_id(year_month):
    # 서버에 업로드된 정보
    file_information_url = 'https://kadx.co.kr:9090/t/41a41690-595f-11eb-8fb9-7f0e72446d5e'
    data_list = requests.get(file_information_url).json()
    file_id = ''
    for data in data_list:
        if year_month in data['fileName']:
            file_id = data['fileID']              
            break
    return file_id

# 파일 다운로드
def download(url):
    return requests.get(url)

# 파일객체를 S3에 파일로 put
def upload_to_s3(s3_file_name, content):

    bucket_name = 'sunjae-test-bucket'   # S3 버킷 이름

    # S3 클라이언트 생성
    s3_client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    # 파일 업로드
    try:
        s3_client.put_object(Bucket=bucket_name, Key=s3_file_name, Body=content)
        print(f"'{s3_file_name}' -> '{bucket_name}/{s3_file_name}' 업로드 완료")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("PARAMETER ERROR : python [filename] [yearmonth]\n ex) python download_and_S3_put.py 202403 ")
    elif len(sys.argv) > 2:
        print("PARAMETER ERROR : python [filename] [yearmonth]\n ex) python download_and_S3_put.py 202403 ")
    elif len(sys.argv[1]) != 6:
        print("년(4자리)월(2자리) 총 6자리 숫자가 인자로 입력되어야 합니다.")
    else:
        ym = sys.argv[1]
        year_month = f'{ym[0:4]}년 {ym[4:]}월' # 다운로드 받고자 하는 년,월 입력. 형식 : "0000년 00월"
        
        file_id = find_file_id(year_month)
        url = 'https://kadx.co.kr:9090/dl/'+file_id
        if file_id != '':
            res = download(url)
            if res.status_code == 200:
                file_name = 'project/'+year_month[:4]+year_month[6:8]+'.csv'
                upload_to_s3(file_name,  res.content)
        else:
            print("서버에 해당 년/월의 파일이 존재하지 않습니다.")




    
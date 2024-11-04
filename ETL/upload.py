import boto3
import os
from botocore.exceptions import NoCredentialsError

# AWS S3에 접근하기 위한 자격 증명 설정
ACCESS_KEY = os.getenv('S3_ACCESS_KEY')  # 환경변수 값
SECRET_KEY = os.getenv('S3_SECRET_KEY')  # 환경변수 값

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


current_directory = os.getcwd() # 현재 경로
files = os.listdir(current_directory) # 파일 목록 읽기
csv_files = [file for file in files if file.endswith('.csv')] # 모든 csv파일 이름 리스트

# csv파일 리스트 순회하며 S3적재
for file in csv_files:
    file_name = file        # 로컬 파일 경로
    bucket_name = 'sunjae-test-bucket'   # S3 버킷 이름
    object_name = f'project/{file_name}' # S3에 저장될 파일 경로 및 이름 (옵션)
    upload_to_s3(file_name, bucket_name, object_name)
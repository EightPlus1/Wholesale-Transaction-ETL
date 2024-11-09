import snowflake.connector
import os

# Snowflake 연결 설정
conn = snowflake.connector.connect(
    user='유저', # 유저 입력
    password='패스워드', # 패스워드 입력
    account='xgrrapq-prb41357',
    warehouse='COMPUTE_WH',
    database='DEV',
    schema='RAW_DATA'
)

AWS_KEY_ID = os.getenv('SNOWFLAKE_AWS_KEY_ID')  # 환경변수 값
AWS_SECRET_KEY = os.getenv('SNOWFLAKE_AWS_KEY_SECRET')  # 환경변수 값

if __name__ == '__main__':
    table_name="" # 테이블명 입력
    file_name=""  # 파일명 입력
    try:
        with conn.cursor() as cursor:
            # 테이블 생성
            cursor.execute(f"""
                           CREATE TABLE dev.raw_data.{table_name} (
                                컬럼1   타입,
                                컬럼2   타입,
                                컬럼3   타입
                           )
                           """)
            
            # 데이터 적재
            cursor.execute(f"""
                           COPY INTO dev.raw_data.{table_name} 
                            FROM 's3://sunjae-test-bucket/project/{file_name}'
                            credentials=(AWS_KEY_ID={AWS_KEY_ID} AWS_SECRET_KEY={AWS_SECRET_KEY})
                            FILE_FORMAT = (type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF = ('', 'NULL'));
                           """)
            

    finally:
        # 연결 종료
        conn.close()

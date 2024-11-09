# 농수산물 도매시장 거래 데이터 ETL 코드
- 1번(일일) 방식으로 데이터를 수집하거나 2번(월단위) 방식으로 선택하여 데이터를 수집 적재
- snowflake COPY명령어는 snowflake 워크스페이스에서 별도 실행 가능

## 1. 정산 API 호출(일별 데이터 다운로드)
- 파일명 : ETL/download_and_S3_put_daily.py
- 의존 라이브러리 : pandas, boto3
- 파라미터 : url, 서비스키, api타입, [페이지넘버, 도매시장코드, 정산일자]
- 실행방법 : 
    1) 코드상 파라미터를 적절하게 입력
    2) python3 ./ETL/download_sale_daily.py [일자 8자리] 커맨드 실행

## 2. 월단위 파일 다운로드 후 S3적재
- 파일명 : ETL/download_and_S3_put_monthly.py
- 의존 라이브러리 : boto3
- 실행방법 :
    1) python3 ./ETL/download_and_S3_put_monthly.py [년월 6자리] 커맨드 실행

## 3. snowflake 테이블 생성
- 파일명 : ETL/load_snowflake.py
- 의존 라이브러리 : snowflake
- 실행방법 :
    1) 코드 내에서 유저, 패스워드, 테이블명, 파일명, DDL문 작성
    2) python3 ./ETL/load_snowflake.py


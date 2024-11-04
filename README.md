# 농수산물 도매시장 거래 데이터 ETL 코드

## 1. API 호출
- 파일명 : ETL/api.py
- 파라미터 : url, 서비스키, api타입, [페이지넘버, 도매시장코드, 정산일자]
- 실행방법 : 
    1) 코드상 파라미터를 적절하게 입력
    2) python3 ./ETL/api.py 커맨드 실행

## 2. csv to S3
- 파일명 : upload.py
- 실행방법 :
    1) S3 액세스 키, 시크릿 키 환경변수 설정
    2) python3 ./ETL/upload.py 커맨드 실행


## 3. snowflake 테이블 생성


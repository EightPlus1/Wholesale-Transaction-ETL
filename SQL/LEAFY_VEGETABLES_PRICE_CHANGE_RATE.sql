-- 2월~9월까지 전월 대비 대분류 평균가 등락률  
CREATE TABLE DEV.ANALYTICS.LEAFY_VEGETABLES_PRICE_CHANGE_RATE AS
SELECT 
    month,
    PDLT_NM,
    avg_price,
    prev_avg_price,
    CASE 
        WHEN prev_avg_price IS NOT NULL 
        THEN ROUND((avg_price - prev_avg_price) / prev_avg_price * 100, 2) 
        ELSE NULL 
    END AS price_change_rate
FROM 
    (SELECT 
        month,
        PDLT_NM,
        avg_price,
        LAG(avg_price) OVER (PARTITION BY PDLT_NM ORDER BY MONTH) AS prev_avg_price
    FROM (
        SELECT 
            TO_CHAR(TO_DATE(B.AUC_YMD, 'YYYYMMDD'), 'YYYYMM') AS month,
            B.PDLT_NM,
            AVG(B.PRCE) AS avg_price    
        FROM 
            DEV.RAW_DATA.GOODS as A
            JOIN DEV.RAW_DATA.SALE  as B 
            on A.PDLT_CODE = B.PDLT_CODE and A.SPCS_CODE = B.SPCS_CODE
        WHERE
            A.LARGE_CODE = '10'
        GROUP BY 1,2))
WHERE 
    prev_avg_price IS NOT NULL
ORDER BY 
    1,2;
;
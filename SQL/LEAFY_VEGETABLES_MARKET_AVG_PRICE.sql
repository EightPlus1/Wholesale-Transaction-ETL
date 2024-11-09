-- large_code = '10'
-- 전체 기간 시장별 엽경채류 평균 도매가격
CREATE OR REPLACE TABLE DEV.ANALYTICS.LEAFY_VEGETABLES_MARKET_AVG_PRICE AS
WITH sale_filtered AS (
    SELECT *, CAST(PRCE / NULLIF(KG_UNIT_CNVR_QYT, 0) AS INT) AS price_per_kg
    FROM dev.raw_data.sale
    WHERE LEFT(PDLT_CODE, 2) = '10' AND WHSL_MRKT_NM IS NOT NULL
),
goods_raw_filtered AS (
    SELECT LARGE, LARGENAME
    FROM dev.raw_data.goods_raw
    WHERE LARGE = '10'
    GROUP BY LARGE, LARGENAME
)
SELECT s.WHSL_MRKT_NM,
       g.LARGENAME,
			 Round(AVG(s.price_per_kg), 0) AS avg_price_per_kg
FROM sale_filtered AS s
JOIN goods_raw_filtered AS g
ON LEFT(s.PDLT_CODE, 2) = g.LARGE
GROUP BY s.WHSL_MRKT_NM, g.LARGENAME
ORDER BY avg_price_per_kg DESC;
-- 도매시장별 엽경채류 품목별 거래 금액
CREATE TABLE DEV.ANALYTICS.LEAFY_VEGETABLES_MARKET_AMOUNT_BY_CATEGORY AS
select b.whsl_mrkt_nm, b.pdlt_nm, sum(b.prce) as sum_of_price
  from dev.raw_data.goods as a
  join dev.raw_data.sale  as b on a.pdlt_code = b.pdlt_code and a.spcs_code = b.spcs_code
where b.whsl_mrkt_nm is not null
  and a.large_code = '10'
group by 1,2
order by 1 asc, 3 desc;
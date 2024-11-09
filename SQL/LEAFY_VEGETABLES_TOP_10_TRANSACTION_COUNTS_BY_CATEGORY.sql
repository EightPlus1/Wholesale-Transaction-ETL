-- 엽경채류 중 거래횟수가 가장 많은 품목 10건
CREATE TABLE DEV.ANALYTICS.LEAFY_VEGETABLES_TOP_10_TRANSACTION_COUNTS_BY_CATEGORY AS
select b.spcs_nm, count(*) cnt
  from dev.raw_data.goods as a
  join dev.raw_data.sale  as b on a.pdlt_code = b.pdlt_code and a.spcs_code = b.spcs_code
 where a.large_code = '10'
   and b.whsl_mrkt_nm is not null
group by  b.spcs_nm
order by 2 desc
limit 10;
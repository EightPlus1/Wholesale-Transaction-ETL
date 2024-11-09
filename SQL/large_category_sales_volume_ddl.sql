create table dev.analytics.large_category_sales_volume as
select to_char(to_date(b.auc_ymd, 'yyyymmdd'), 'yyyy-mm') as month, 
       a.largename,
       b.pdlt_nm,
       b.spcs_nm,
       count(*) as volume
  from dev.raw_data.goods as a 
  join dev.raw_data.sale as b on a.pdlt_code = b.pdlt_code and a.spcs_code = b.spcs_code
where whsl_mrkt_nm is not null
  and wmk_corp_nm is not null
group by 1,2,3,4
;
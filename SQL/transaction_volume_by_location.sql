create table dev.analytics.cnt_location as
select  to_char(to_date(a.auc_ymd,'yyyymmdd'),'yyyy-mm') as month,
        b.latitude,
        b.longitude,
        count(*) cnt
  from dev.raw_data.sale as a join dev.raw_data.whsal as b on a.whsl_mrkt_code = b.codeid
group by 1,2,3
;
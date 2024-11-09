create table dev.raw_data.goods as
select  large as large_code,
        largename,
        concat(large,mid) as pdlt_code,
        midname,
        concat(large,mid,small) as spcs_code,
        goodname
  from dev.raw_data.goods_raw
where gubn is not null
;
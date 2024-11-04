CREATE TABLE dev.raw_data.sale (
    auc_ymd VARCHAR(8),                                  -- 경매일자
    whsl_mrkt_code VARCHAR(10),                   -- 도매시장코드
    whsl_mrkt_nm VARCHAR(100),                    -- 도매시장명
    wmk_corp_code VARCHAR(20),                     -- 도매시장안법인코드
    wmk_corp_nm VARCHAR(100),                      -- 도매시장안법인명
    pdlt_code VARCHAR(10),                         -- 품목코드
    pdlt_nm VARCHAR(100),                          -- 품목명
    spcs_code VARCHAR(10),                         -- 품종코드
    spcs_nm VARCHAR(100),                          -- 품종명
    unit_code VARCHAR(10),                         -- 단위코드
    unit_nm VARCHAR(100),                          -- 단위명
    pkg_stle_code VARCHAR(10),                     -- 포장형태코드
    pkg_stle_nm VARCHAR(100),                      -- 포장형태명
    nop_code VARCHAR(10),                          -- 포장개수코드
    nop_nm VARCHAR(100),                           -- 포장개수명
    mtc_grad_code VARCHAR(10),                     -- 산지등급코드
    mtc_grad_nm VARCHAR(100),                      -- 산지등급명
    mtc_nm VARCHAR(100),                           -- 산지명
    unit_qyt BIGINT,                                  -- 단위수량
    prce BIGINT,                           -- 가격
    etl_ldg_dt VARCHAR(15),                          -- ETL적재일시
    kg_unit_cnvr_qyt DECIMAL(10, 2)               -- KG단위변환수량
);

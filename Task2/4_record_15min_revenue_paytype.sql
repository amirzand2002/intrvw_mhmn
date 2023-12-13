SELECT
  date_bin('15 minutes', "RECORD_DATE", TIMESTAMP '2001-01-01') AS date_time,
  pt.value AS paytype_value,
  SUM("DEBIT_AMOUNT_42" * POWER(10, -4))::INT AS total_revenue,
  COUNT(*) AS record_count
FROM "REF_CBS_SMS2" rcs
INNER JOIN paytype pt ON rcs."PAYTYPE_515"  = pt.pay_type
GROUP BY date_time, rcs."PAYTYPE_515" , pt.value;

-- this query runs in 292ms.
SELECT
  date_bin('15 minutes', "RECORD_DATE", TIMESTAMP '2001-01-01') AS date_time,
  "PAYTYPE_515" AS payment,
  SUM("DEBIT_AMOUNT_42" * POWER(10, -4))::INT AS total_revenue,
  MAX("DEBIT_AMOUNT_42" * POWER(10, -4))::INT AS max_revenue,
  MIN("DEBIT_AMOUNT_42" * POWER(10, -4))::INT AS min_revenue
FROM "REF_CBS_SMS2" rcs
GROUP BY date_time, payment;
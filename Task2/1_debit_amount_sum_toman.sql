-- this query took 296ms to complete.
SELECT
  date_trunc('day',"RECORD_DATE") as date,
  SUM("DEBIT_AMOUNT_42"*POWER(10,-4))::int AS total_income
FROM "REF_CBS_SMS2" rcs
GROUP BY date
ORDER BY date ASC;
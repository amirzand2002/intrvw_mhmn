-- this query took 267ms to complete.

SELECT
	date_bin('15 minutes',"RECORD_DATE"  , TIMESTAMP '2001-01-01') as date_time,
	"PAYTYPE_515" as payment,
	sum("DEBIT_AMOUNT_42"*power(10,-4))::int as revenue 
from "REF_CBS_SMS2" rcs 
group by date_time,payment;



-- this query took 483ms to complete.
SELECT date_trunc('hour', "RECORD_DATE") + date_part('minute', "RECORD_DATE")::int / 15 * interval '15 min' AS minute
      , "PAYTYPE_515" , sum("DEBIT_AMOUNT_42" * power(10,-4))::int as revenue
FROM "REF_CBS_SMS2" rcs
GROUP BY 1, "PAYTYPE_515"
ORDER BY 1 asc;
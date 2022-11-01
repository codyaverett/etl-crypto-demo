
-- Windows at the earliest times will have a smaller average aggregate counts 
-- due to lack of data to calculate the average.

SELECT time
	, price
	, AVG(price) OVER(ORDER BY time
      ROWS BETWEEN 10 PRECEDING AND CURRENT ROW)
    	AS moving_average_11
	, AVG(price) OVER(ORDER BY time
      	ROWS BETWEEN 20 PRECEDING AND CURRENT ROW)
    	AS moving_average_21
	, AVG(price) OVER(ORDER BY time
      	ROWS BETWEEN 49 PRECEDING AND CURRENT ROW)
    	AS moving_average_50
  FROM public.asset_price
  WHERE pair_id = 1 and time > NOW() - INTERVAL '1 day'
  ORDER BY time DESC;
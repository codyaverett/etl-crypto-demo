SELECT 
  price.id AS "id"
  , price.time AS "time"
  , price.price AS "price"
  , CONCAT(asset1.symbol,'/',asset2.symbol) AS "pair"
FROM public.asset_price AS price
JOIN public.asset_tradingpair AS tradingpair ON tradingpair.id = price.pair_id
JOIN public.asset AS asset1 ON tradingpair.numerator_id = asset1.id
JOIN public.asset AS asset2 ON tradingpair.denominator_id = asset2.id
--WHERE asset_tradingpair.denominator_id = 1
--LIMIT 1000
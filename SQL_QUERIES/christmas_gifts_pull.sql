create or replace table "christmas_gifts_pull" as

select 
    "28/10/22"."theme",
    "28/10/22"."set_number_and_name",
    '2022-10-28' as "scraping_date",
    "28/10/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "28/10/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-10-28" as "28/10/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "31/10/22"."theme",
    "31/10/22"."set_number_and_name",
    '2022-10-31' as "scraping_date",
    "31/10/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "31/10/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-10-31" as "31/10/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "01/11/22"."theme",
    "01/11/22"."set_number_and_name",
    '2022-11-01' as "scraping_date",
    "01/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "01/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-01" as "01/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "02/11/22"."theme",
    "02/11/22"."set_number_and_name",
    '2022-11-02' as "scraping_date",
    "02/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "02/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-02" as "02/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "02/11/22"."theme",
    "02/11/22"."set_number_and_name",
    '2022-11-02' as "scraping_date",
    "02/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "02/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-02" as "02/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "03/11/22"."theme",
    "03/11/22"."set_number_and_name",
    '2022-11-03' as "scraping_date",
    "03/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "03/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-03" as "03/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "04/11/22"."theme",
    "04/11/22"."set_number_and_name",
    '2022-11-04' as "scraping_date",
    "04/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "04/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-04" as "04/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "05/11/22"."theme",
    "05/11/22"."set_number_and_name",
    '2022-11-05' as "scraping_date",
    "05/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "05/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-05" as "05/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')

    union all
    
    select 
    "06/11/22"."theme",
    "06/11/22"."set_number_and_name",
    '2022-11-06' as "scraping_date",
    "06/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "06/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-06" as "06/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "07/11/22"."theme",
    "07/11/22"."set_number_and_name",
    '2022-11-07' as "scraping_date",
    "07/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "07/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-07" as "07/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "08/11/22"."theme",
    "08/11/22"."set_number_and_name",
    '2022-11-08' as "scraping_date",
    "08/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "08/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-08" as "08/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')

    union all
    
    select 
    "09/11/22"."theme",
    "09/11/22"."set_number_and_name",
    '2022-11-09' as "scraping_date",
    "09/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "09/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-09" as "09/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "10/11/22"."theme",
    "10/11/22"."set_number_and_name",
    '2022-11-10' as "scraping_date",
    "10/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "10/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-10" as "10/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    
    union all
    
    select 
    "11/11/22"."theme",
    "11/11/22"."set_number_and_name",
    '2022-11-11' as "scraping_date",
    "11/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "11/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-11" as "11/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "12/11/22"."theme",
    "12/11/22"."set_number_and_name",
    '2022-11-12' as "scraping_date",
    "12/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "12/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-12" as "12/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "13/11/22"."theme",
    "13/11/22"."set_number_and_name",
    '2022-11-13' as "scraping_date",
    "13/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "13/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-13" as "13/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "14/11/22"."theme",
    "14/11/22"."set_number_and_name",
    '2022-11-14' as "scraping_date",
    "14/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "14/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-14" as "14/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "15/11/22"."theme",
    "15/11/22"."set_number_and_name",
    '2022-11-15' as "scraping_date",
    "15/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "15/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-15" as "15/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "16/11/22"."theme",
    "16/11/22"."set_number_and_name",
    '2022-11-16' as "scraping_date",
    "16/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "16/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-16" as "16/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "17/11/22"."theme",
    "17/11/22"."set_number_and_name",
    '2022-11-17' as "scraping_date",
    "17/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "17/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-17" as "17/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "18/11/22"."theme",
    "18/11/22"."set_number_and_name",
    '2022-11-18' as "scraping_date",
    "18/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "18/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-18" as "18/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "19/11/22"."theme",
    "19/11/22"."set_number_and_name",
    '2022-11-19' as "scraping_date",
    "19/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "19/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-19" as "19/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
      
    union all
    
    select 
    "19/11/22"."theme",
    "19/11/22"."set_number_and_name",
    '2022-11-19' as "scraping_date",
    "19/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "19/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-19" as "19/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "20/11/22"."theme",
    "20/11/22"."set_number_and_name",
    '2022-11-20' as "scraping_date",
    "20/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "20/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-20" as "20/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all
    
    select 
    "21/11/22"."theme",
    "21/11/22"."set_number_and_name",
    '2022-11-21' as "scraping_date",
    "21/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "21/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-21" as "21/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    union all 
   
    select 
    "22/11/22"."theme",
    "22/11/22"."set_number_and_name",
    '2022-11-22' as "scraping_date",
    "22/11/22"."price" as "price",
    round("price" * '24.34',2) as "price CZK",
    "22/11/22"."rating" as "rating"
    from "scraping-data-all-sets-2022-11-22" as "22/11/22"
    where ("theme" ilike '%Harry Potter%' or "set_number_and_name" ilike '%Harry Potter%') 
    or ("theme" ilike '%Star Wars%' or "set_number_and_name" ilike '%Star Wars%')
    or ("theme" ilike 'City%')
    
    
-- Table "christmas_gifts_pull" successfully created.


update "christmas_gifts_pull" set "rating" = NULL where "rating" = 'NULL'
-- number of rows updated 52


create or replace table "christmas_gifts_pull_prices" as
select 
    "theme",
    "set_number_and_name",
    "price CZK"
from "christmas_gifts_pull"
where "price CZK" <= '2500' and "scraping_date" = '2022-11-22'
-- Table "christmas_gifts_pull_prices" successfully created.


create or replace table "christmas_gifts_pull_ratings" as
select 
    "theme",
    "set_number_and_name",
    avg("rating") as "rating_average"
from "christmas_gifts_pull"
group by "theme","set_number_and_name"
order by "rating_average" desc nulls last
-- Table "christmas_gifts_pull_ratings" successfully created.


create or replace table "christmas_gifts_pull_100" as
select "christmas_gifts_pull_prices".*, "christmas_gifts_pull_ratings"."rating_average"
from "christmas_gifts_pull_prices"
left join "christmas_gifts_pull_ratings" 
on "christmas_gifts_pull_prices"."set_number_and_name" = "christmas_gifts_pull_ratings"."set_number_and_name"
where "rating_average" >= '4.7'
-- Table "christmas_gifts_pull_100" successfully created.


create or replace table "rebrickable_number_of_parts" as
select 
    "set_num",
    split("set_num", '-')[0] as "set_number_brickeconomy_format", 
    "name",
    replace(replace(replace(replace("name", ':', ''), '’', "'"), ')',''), '(', '') as "set_name_brickeconomy_format",
    "set_number_brickeconomy_format" || ' ' || "set_name_brickeconomy_format" as "set_number_and_name_brickeconomy_format",
    "num_parts" 
from "sets"
-- Table "rebrickable_number_of_parts" successfully created.


create or replace table "christmas_gifts_final_pull"  as
select 
"christmas_gifts_pull_100".*,
"rebrickable_number_of_parts"."set_number_and_name_brickeconomy_format",
"rebrickable_number_of_parts"."num_parts" 
from "christmas_gifts_pull_100" 
left join "rebrickable_number_of_parts" 
on "rebrickable_number_of_parts"."set_number_and_name_brickeconomy_format" = "christmas_gifts_pull_100"."set_number_and_name"
where "rebrickable_number_of_parts"."set_number_and_name_brickeconomy_format" is not null
and  "price CZK" >= '500'
order by "price CZK" desc, "num_parts" desc
-- Table "christmas_gifts_final_pull" successfully created.

select * from "christmas_gifts_final_pull"
-- 68 rows
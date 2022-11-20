/*
These are several queries used for the analysis and visualisations.
See the source files: https://rebrickable.com/downloads/
*/


-- Those are the most popular parts
select 
        "inventory-parts"."part_num",
        "parts"."name",
        count(*) as "frequency", 
        sum("quantity") as "total_number_all_inventories"
from "inventory-parts"
left join "parts" on "parts"."part_num" = "inventory-parts"."part_num"
group by "inventory-parts"."part_num", "parts"."name"
having "inventory-parts"."part_num" NOT LIKE '%dummy%'
order by "total_number_all_inventories" desc
limit 10


-- Finding sets and parts with the rarest LEGO colors
select
    "inventory-parts"."part_num",
    "parts"."name",
    "inventory-parts"."color_id",
    "colors"."name",
    "inventory_id", 
    "inventories"."set_num", 
    "sets"."name", 
    "sets"."year"
from "inventory-parts" 
left join "inventories" on "inventories"."id" = "inventory-parts"."inventory_id"
left join "sets" on "sets"."set_num" = "inventories"."set_num"
left join "colors" on "inventory-parts"."color_id" = "colors"."id"
left join "parts" on "parts"."part_num" = "inventory-parts"."part_num"
where "inventory-parts"."color_id" IN (select
                      "color_id"
                      from "inventory-parts"
                      left join "colors" on "inventory-parts"."color_id" = "colors"."id"
                      group by "color_id","colors"."name" 
                      having sum("quantity") = 1)


--- Those are the oldest parts
select 
    "inventory-parts"."part_num"  
from "sets"
left join "inventories" on "inventories"."set_num" = "sets"."set_num"
left join "inventory-parts" on "inventory-parts"."inventory_id" = "inventories"."id"
where "year" = '1949'
group by "part_num"


-- Those are the most colorful parts
create or replace table "most_colorful_parts" AS
select 
    "elements"."part_num" as "part_id", 
    "parts"."name" as "part_name", 
    count (distinct "color_id") as "number_of_colors"
from "elements"
left join "parts" on "parts"."part_num" = "elements"."part_num"
where "color_id" not in ('9999', '-1') and "elements"."part_num" NOT LIKE '%dummy%'
group by "elements"."part_num", "parts"."name"
order by "number_of_colors" DESC
LIMIT 15;

select * from "most_colorful_parts"


-- The most colorful LEGO set
SELECT 
    "set_num",
    "name"
FROM "sets" 
WHERE "set_num" = 
(SELECT "set_num" FROM "inventories"
WHERE "id" = 
      (SELECT "inventory_id"
       FROM "inventory-parts" 
       WHERE "color_id" NOT IN (-1, 9999)
       GROUP BY "inventory_id"
       ORDER BY COUNT (DISTINCT "color_id") DESC
       LIMIT 1))
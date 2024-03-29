SELECT
	*
FROM
	superstore_data;

SELECT
	id, education 
FROM
	superstore_data;

select
	*
from
	superstore_data
where
	kidhome > 3;

select
	*
from
	superstore_data
where
	kidhome = 2;

select
	*
from
	superstore_data
where
	kidhome = 2 or teenhome = 2;

select
	*
from
	superstore_data
where
	(kidhome != 1
		and teenhome = 1)
	or
	(mntfruits >100
		and mntfishproducts > 100);
	
select
	id,
	kidhome,
	teenhome,
	kidhome + teenhome as total_children,
	mntwines + mntsweetproducts as not_healty_spend
from
	superstore_data sd;

-- using between
select
	*
from
	superstore_data
where
	year_birth between 1970 and 1980;


select distinct education 
from superstore_data sd ;


select * from superstore_data sd 
where income is null;

select * from superstore_data sd 
where income is not null;

select round(income/1000.0, 1) as income_in_K
from superstore_data sd ;

select distinct lower(education)
from superstore_data sd ;

select * from superstore_data sd ;

select marital_status || ' ' || income 
from superstore_data sd ;

select * from superstore_data sd 
where lower(marital_status) = 'single';

select * from superstore_data sd 
where marital_status like 'Single';

select * from superstore_data sd 
where marital_status like '%ng%';

select * from superstore_data sd 
where marital_status like 'S%n%';

select * from superstore_data sd 
where marital_status like 'S%';

select * from superstore_data sd 
where marital_status ilike '%e%';

select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by income ;

select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by income asc;

select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by income desc;


select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by year_birth, income ;

select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by (year_birth, income) desc ;

select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by year_birth desc, income asc;

select year_birth, income , education 
from superstore_data
where mntgoldprods = 0
order by year_birth desc, income asc
limit 10 offset 20;

select count(*) 
from superstore_data;

select count(id) 
from superstore_data;

select count(income) 
from superstore_data;

select sum(mntwines), avg(mntwines), stddev(mntwines),
	min(mntwines), max(mntwines)
from superstore_data sd ;

select min(mntsweetproducts), max(mntsweetproducts)
from superstore_data
where kidhome > 1;


select education, count(id)  
from superstore_data
group by education ;

select
	marital_status,
	min(kidhome + teenhome),
	max(kidhome + teenhome),
	round(avg(kidhome+teenhome), 1) as avg_children
from
	superstore_data sd
group by
	marital_status ;


select
	lower(education) as edu,
	marital_status,
	round(avg(income)) as avg_income
from
	superstore_data
group by
	edu,
	marital_status
order by 
	edu, marital_status
limit 10
offset 5;


select
	lower(education) as edu,
	marital_status,
	round(avg(income)) as avg_income
from
	superstore_data
where income > 9000
group by
	edu,
	marital_status
order by 
	edu, marital_status;


select
	lower(education) as edu,
	marital_status,
	round(avg(income)) as avg_income
from
	superstore_data
where kidhome + teenhome = 2
group by
	edu,
	marital_status
having round(avg(income)) > 30000
order by 
	edu, marital_status;


select id, year_birth, 2023-year_birth as age
from superstore_data;


select now();

select id, year_birth, extract(year from now())-year_birth as age
from superstore_data;


select year_birth  from superstore_data
where year_birth = 
	(select max(year_birth) from superstore_data);


with max_year as (
	select max(year_birth)
	from superstore_data
)
select * from superstore_data sd 
where year_birth = (select * from max_year);



-- CRUD

insert
	into
	superstore_data
(id,
	year_birth,
	education)
values
(11112,
'2000',
'Master');

select * from superstore_data sd 
where id=11111;






insert
	into
	superstore_data 
	(id,
	year_birth,
	education,
	marital_status,
	income,
	kidhome,
	teenhome,
	dt_customer,
	recency,
	mntwines,
	mntfruits,
	mntmeatproducts,
	mntfishproducts,
	mntsweetproducts,
	mntgoldprods,
	numdealspurchases,
	numwebpurchases,
	numcatalogpurchases,
	numstorepurchases,
	numwebvisitsmonth,
	response,
	complain)
values(0,
0,
'',
'',
0,
0,
0,
'',
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0);

select * from superstore_data sd ;

insert into superstore_data 
values (222222, 1999 );



update
	superstore_data
set
	year_birth = 2000
where id = 222222;

select * from superstore_data sd where id=222222;

update superstore_data 
set income = 0
where income is null;

update superstore_data 
set
	recency = 10, numwebvisitsmonth = 100
where income =0;


update superstore_data 
set
	education = upper(education)
where education = 'Master';


delete from superstore_data 
where id = 222222;


delete from superstore_data 
where year_birth = 1970;




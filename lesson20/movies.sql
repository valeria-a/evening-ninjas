-- id
-- name
-- release_date
-- description
-- genre
-- duration

-- director
-- actors



--create table movies (
--	--primary key
--	id serial primary key,
--	name varchar(256) not null,
--	release_date date not null,
--	description varchar,
--	genre varchar(64) not null,
--	duration smallint check (duration > 0)
--
--);


--drop table movies;


create table directors (
	--primary key
	id serial primary key,
	name varchar(256) not null,
	birth_date date,
	oscars smallint default 0
);


create table movies (
	--primary key
	id serial primary key,
	name varchar(256) not null,
	release_date date not null,
	description varchar,
	genre varchar(64) not null,
	duration smallint check (duration > 0),
	director_id int not null,
	foreign key (director_id) references directors(id)
);



INSERT INTO movies
("name", release_date, description, genre, duration, director_id)
values
('aaaa', '2000-12-12', 'sdfgdgdfgadfg', 'comedy', 100, 1);

select * from directors d ;



select
	d.name,
	count(d.id)
from
	movies m
join
	directors d
on
	m.director_id = d.id
where
	oscars > 5
group by
	director_id,
	d."name"
;



select d.name, m.name from movies m
join directors d
on m.director_id = d.id ;

select
	d.name,
	m.name
from
	movies m left join directors d
on
	m.director_id = d.id ;

select
	d.name,
	m.name
from
	movies m right join directors d
on
	m.director_id = d.id ;

select
	d.name,
	m.name
from
	movies m full join directors d
on
	m.director_id = d.id ;


select *  from movies m , directors d ;

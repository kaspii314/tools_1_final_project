/*
 * What problem you are trying to solve?
 * Are certain mediums more popular in particular time periods, cultures, or geographies?
 * Is there a pattern or trend in types of art being acquired by The Met?
 * Can we identify defining characteristics that determine whether artwork is considered a “highlight” piece?
 *  
 */

-- remove first line
delete from open_access
where object_number = 'Object Number';

-- duplicates
select sum(1)
from (
	select object_id, count(*) as cnt
	from open_access
	group by object_id
	having count(*) > 1
	-- order by count(*) desc
) t
;

select *
from open_access;

/*
 * BOOLEAN
 */

-- is_highlight
select distinct is_highlight
from open_access;

-- is_timeline_work
select distinct is_timeline_work
from open_access;

-- is_public_domain
select distinct is_public_domain
from open_access;


/*
 * NUMERIC
 */

-- object_id -- PRIMARY KEY
select cast(object_id as int)
from open_access;

-- gallery_number
select gallery_number, count(*) as cnt
from open_access
where is_highlight = True
group by gallery_number
order by count(*) desc;

select gallery_number, count(*) as cnt
from open_access
where gallery_number !~ '^[0-9]*$'
group by gallery_number
order by count(*) desc;

-- accessionyear
select accessionyear, accessionyear_clean, count(*) as cnt
from open_access
where accessionyear !~ '^[0-9]*$'
group by accessionyear, accessionyear_clean
order by count(*) desc;

-- artist_begin_date
select artist_begin_date, artist_begin_date_clean,  count(*) as cnt
from open_access
where artist_begin_date !~ '^[0-9]*$'
group by artist_begin_date, artist_begin_date_clean
order by count(*) desc;

-- artist_end_date
select artist_end_date, artist_end_date_clean,  count(*) as cnt
from open_access
where artist_end_date !~ '^[0-9]*$'
group by artist_end_date, artist_end_date_clean
order by count(*) desc;


select *
from open_access
where gallery_number is null and is_highlight = true


/*
 * IMPORTANT STRINGS
 * 
 */

-- department
select department, count(*) as cnt
from open_access
group by department
order by department;

-- classification
select sum(1) 
from(
	select classification, count(*) as cnt
	from open_access
	where classification is null
	group by classification
	order by count(*) desc
) t;

-- object_name
select sum(1) 
from(
	select object_name, count(*) as cnt
	from open_access
	where object_name is null
	group by object_name
	order by count(*) desc
) t;

-- period

-- culture

-- department

-- artist_display_name

-- artist_nationality

-- medium

-- geography

-- tags



/*
 * Variables I want to analyze
 * is_highlight
 * department
 * accessionyear
*/
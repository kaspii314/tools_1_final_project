/*
 * CREATE MET TABLES
 * 
*/

drop table if exists open_access;

create table open_access(
object_number text
,is_highlight bool
,is_timeline_work bool
,is_public_domain bool
,object_id int
,gallery_number text
,department text
,accessionyear text
,object_name text
,title text
,culture text
,period text
,dynasty text
,reign text
,portfolio text
,constituent_id text
,artist_role text
,artist_prefix text
,artist_display_name text
,artist_display_bio text
,artist_suffix text
,artist_alpha_sort text
,artist_nationality text
,artist_begin_date text
,artist_end_date text
,artist_gender text
,artist_ulan_url text
,artist_wikidata_url text
,object_date text
,object_begin_date text
,object_end_date text
,medium text
,dimensions text
,credit_line text
,geography_type text
,city text
,state text
,county text
,country text
,region text
,subregion text
,locale text
,locus text
,excavation text
,river text
,classification text
,rights_and_reproduction text
,link_resource text
,object_wikidata_url text
,metadata_date text
,repository text
,tags text
,tags_aat_url text
,tags_wikidata_url text
,accessionyear_clean int
,artist_begin_date_clean int
,artist_end_date_clean int
,primary key (object_id)
);

/*
-- Must have header in text file because there are some columns that are always blank.
\COPY open_access(object_number,is_highlight,is_timeline_work,is_public_domain,object_id,gallery_number,department,accessionyear,object_name,title,culture,period,dynasty,reign,portfolio,constituent_id,artist_role,artist_prefix,artist_display_name,artist_display_bio,artist_suffix,artist_alpha_sort,artist_nationality,artist_begin_date,artist_end_date,artist_gender,artist_ulan_url,artist_wikidata_url,object_date,object_begin_date,object_end_date,medium,dimensions,credit_line,geography_type,city,state,county,country,region,subregion,locale,locus,excavation,river,classification,rights_and_reproduction,link_resource,object_wikidata_url,metadata_date,repository,tags,tags_aat_url,tags_wikidata_url
,accessionyear_clean,artist_begin_date_clean,artist_end_date_clean)
FROM '/Users/kaspii/github/tool1_final_project/data/MetObjects_clean.csv' DELIMITER '|' csv HEADER;
*/
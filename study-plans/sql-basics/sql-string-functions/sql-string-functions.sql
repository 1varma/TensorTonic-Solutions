-- Write your SQL query here
select
    LOWER(TRIM(respondent)) as respondent_clean,
    length(trim(raw_answer)) as answer_length,
    substring(trim(raw_answer), 1, 20) as answer_preview,
    SPLIT_PART(source_url, '/', 3) as source_domain
from survey_responses
order by respondent_clean asc;
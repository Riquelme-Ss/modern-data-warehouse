select
    date_key,
    full_date,
    day,
    month,
    year,
    quarter,
    month_name,
    day_of_week,
    day_name,
    is_weekend
from {{ source('warehouse', 'dim_date') }}
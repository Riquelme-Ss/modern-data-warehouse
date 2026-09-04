select
    customer_key,
    customer_id,
    customer_name,
    city,
    state,
    created_at,
    email,
    country,
    registration_date,
    customer_segment
from {{ source('warehouse', 'dim_customer') }}
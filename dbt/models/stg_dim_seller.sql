select
    seller_key,
    seller_id,
    seller_name,
    city,
    state,
    created_at,
    store_id,
    hire_date,
    commission_rate
from {{ source('warehouse', 'dim_seller') }}
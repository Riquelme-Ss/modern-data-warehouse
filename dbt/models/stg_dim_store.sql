select
    store_key,
    store_id,
    store_name,
    city,
    state,
    created_at,
    region
from {{ source('warehouse', 'dim_store') }}
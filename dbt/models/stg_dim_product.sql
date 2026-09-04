select
    product_key,
    product_id,
    product_name,
    category,
    brand,
    cost,
    price,
    stock_quantity,
    created_at
from {{ source('warehouse', 'dim_product') }}
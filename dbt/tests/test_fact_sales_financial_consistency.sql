select
    sales_key,
    order_item_id,
    gross_amount,
    discount_amount,
    net_amount
from {{ ref('stg_fact_sales') }}
where abs(
    (gross_amount - discount_amount) - net_amount
) > 0.01
select
    c.customer_key,
    c.customer_id,
    c.customer_name,
    c.city,
    c.state,
    c.country,
    c.customer_segment,

    count(distinct f.order_id) as total_orders,
    sum(f.quantity) as total_units_sold,

    sum(f.gross_amount) as gross_revenue,
    sum(f.discount_amount) as total_discounts,
    sum(f.net_amount) as net_revenue,

    round(
        sum(f.net_amount) / nullif(count(distinct f.order_id), 0),
        2
    ) as average_order_value,

    min(f.order_date) as first_order_date,
    max(f.order_date) as last_order_date

from {{ ref('stg_dim_customer') }} c

left join {{ ref('stg_fact_sales') }} f
    on c.customer_key = f.customer_key

group by
    c.customer_key,
    c.customer_id,
    c.customer_name,
    c.city,
    c.state,
    c.country,
    c.customer_segment
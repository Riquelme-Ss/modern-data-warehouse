select
    p.category,

    count(distinct f.order_id) as total_orders,
    count(distinct f.customer_key) as total_customers,

    sum(f.quantity) as total_units_sold,

    sum(f.gross_amount) as gross_revenue,
    sum(f.discount_amount) as total_discounts,
    sum(f.net_amount) as net_revenue,

    round(
        sum(f.net_amount) / nullif(sum(f.quantity), 0),
        2
    ) as average_unit_revenue

from {{ ref('stg_fact_sales') }} f

inner join {{ ref('stg_dim_product') }} p
    on f.product_key = p.product_key

group by
    p.category

order by
    net_revenue desc

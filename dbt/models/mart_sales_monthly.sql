select
    d.year,
    d.month,
    d.month_name,

    count(distinct f.order_id) as total_orders,
    count(distinct f.customer_key) as total_customers,

    sum(f.quantity) as total_units_sold,

    sum(f.gross_amount) as gross_revenue,
    sum(f.discount_amount) as total_discounts,
    sum(f.net_amount) as net_revenue,

    round(
        sum(f.net_amount) / nullif(count(distinct f.order_id), 0),
        2
    ) as average_order_value

from {{ ref('stg_fact_sales') }} f

inner join {{ ref('stg_dim_date') }} d
    on f.date_key = d.date_key

group by
    d.year,
    d.month,
    d.month_name
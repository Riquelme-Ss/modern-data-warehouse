
# Codigos organizado por comentarios

from pathlib import Path
from datetime import datetime, timedelta
import random

import pandas as pd
from faker import Faker


fake = Faker("pt_BR")
random.seed(42)
Faker.seed(42)


# CONFIGURAÇÕES

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "generated"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_CUSTOMERS = 50_000
NUM_PRODUCTS = 5_000
NUM_STORES = 100
NUM_SELLERS = 1_000
NUM_ORDERS = 500_000


# CONFIGURAÇÕES DE NEGÓCIO

STATES = [
    "PE", "SP", "RJ", "MG", "BA",
    "PR", "SC", "RS", "GO", "CE"
]

REGIONS = {
    "PE": "Nordeste",
    "SP": "Sudeste",
    "RJ": "Sudeste",
    "MG": "Sudeste",
    "BA": "Nordeste",
    "PR": "Sul",
    "SC": "Sul",
    "RS": "Sul",
    "GO": "Centro-Oeste",
    "CE": "Nordeste",
}

CATEGORIES = [
    "Eletrônicos",
    "Informática",
    "Celulares",
    "Casa",
    "Eletrodomésticos",
    "Games",
    "Acessórios",
    "Esportes",
    "Moda",
    "Livros",
]

BRANDS = [
    "Samsung",
    "Apple",
    "Dell",
    "Lenovo",
    "LG",
    "Sony",
    "Xiaomi",
    "Motorola",
    "Asus",
    "Acer",
]

ORDER_STATUSES = [
    "Completed",
    "Processing",
    "Cancelled",
    "Shipped",
]

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "Pix",
    "Boleto",
]

DELIVERY_STATUSES = [
    "Delivered",
    "In Transit",
    "Delayed",
    "Cancelled",
]

CARRIERS = [
    "Correios",
    "Jadlog",
    "Loggi",
    "Total Express",
    "Sequoia",
]


# CUSTOMERS

def generate_customers():

    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        state = random.choice(STATES)

        customers.append({
            "customer_id": f"C{i:06d}",
            "name": fake.name(),
            "email": fake.unique.email(),
            "city": fake.city(),
            "state": state,
            "country": "BR",
            "registration_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
            "customer_segment": random.choices(
                ["Standard", "Premium", "VIP"],
                weights=[70, 25, 5]
            )[0],
        })

    return pd.DataFrame(customers)


# PRODUCTS

def generate_products():

    products = []

    for i in range(1, NUM_PRODUCTS + 1):

        cost = round(random.uniform(20, 5000), 2)

        margin = random.uniform(1.15, 1.60)

        price = round(cost * margin, 2)

        products.append({
            "product_id": f"P{i:06d}",
            "product_name": fake.catch_phrase(),
            "category": random.choice(CATEGORIES),
            "brand": random.choice(BRANDS),
            "cost": cost,
            "price": price,
            "stock_quantity": random.randint(0, 500),
        })

    return pd.DataFrame(products)


# STORES

def generate_stores():

    stores = []

    for i in range(1, NUM_STORES + 1):

        state = random.choice(STATES)

        stores.append({
            "store_id": f"S{i:04d}",
            "store_name": f"Loja {fake.city()} {i}",
            "city": fake.city(),
            "state": state,
            "region": REGIONS[state],
        })

    return pd.DataFrame(stores)


# SELLERS

def generate_sellers():

    sellers = []

    for i in range(1, NUM_SELLERS + 1):

        sellers.append({
            "seller_id": f"V{i:05d}",
            "seller_name": fake.name(),
            "store_id": f"S{random.randint(1, NUM_STORES):04d}",
            "hire_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
            "commission_rate": round(
                random.uniform(0.01, 0.08),
                4
            ),
        })

    return pd.DataFrame(sellers)


# ORDERS

def generate_orders(customers, sellers):

    orders = []

    for i in range(1, NUM_ORDERS + 1):

        customer_id = random.choice(
            customers["customer_id"].tolist()
        )

        seller_id = random.choice(
            sellers["seller_id"].tolist()
        )

        seller_store = sellers.loc[
            sellers["seller_id"] == seller_id,
            "store_id"
        ].iloc[0]

        order_date = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        orders.append({
            "order_id": f"O{i:07d}",
            "customer_id": customer_id,
            "store_id": seller_store,
            "seller_id": seller_id,
            "order_date": order_date,
            "order_status": random.choices(
                ORDER_STATUSES,
                weights=[70, 10, 5, 15]
            )[0],
            "payment_method": random.choice(
                PAYMENT_METHODS
            ),
        })

    return pd.DataFrame(orders)


# ORDER ITEMS

def generate_order_items(orders, products):

    order_items = []

    product_ids = products["product_id"].tolist()

    item_id = 1

    for order_id in orders["order_id"]:

        number_of_items = random.randint(1, 5)

        selected_products = random.sample(
            product_ids,
            number_of_items
        )

        for product_id in selected_products:

            product = products.loc[
                products["product_id"] == product_id
            ].iloc[0]

            quantity = random.randint(1, 4)

            discount = round(
                random.uniform(0, 0.15),
                2
            )

            order_items.append({
                "order_item_id": f"OI{item_id:08d}",
                "order_id": order_id,
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": product["price"],
                "discount": discount,
            })

            item_id += 1

    return pd.DataFrame(order_items)


# PAYMENTS

def generate_payments(orders, order_items):

    payments = []

    totals = (
        order_items
        .assign(
            total=lambda x:
            x["quantity"]
            * x["unit_price"]
            * (1 - x["discount"])
        )
        .groupby("order_id")["total"]
        .sum()
    )

    for i, (_, order) in enumerate(
        orders.iterrows(),
        start=1
    ):

        amount = round(
            totals.get(order["order_id"], 0),
            2
        )

        payment_date = order["order_date"]

        payments.append({
            "payment_id": f"PAY{i:07d}",
            "order_id": order["order_id"],
            "payment_date": payment_date,
            "payment_method": order["payment_method"],
            "payment_status": random.choices(
                ["Approved", "Pending", "Failed"],
                weights=[90, 7, 3]
            )[0],
            "amount": amount,
        })

    return pd.DataFrame(payments)


# DELIVERIES

def generate_deliveries(orders):

    deliveries = []

    for i, (_, order) in enumerate(
        orders.iterrows(),
        start=1
    ):

        shipping_date = order["order_date"] + timedelta(
            days=random.randint(1, 3)
        )

        estimated_delivery = shipping_date + timedelta(
            days=random.randint(3, 10)
        )

        actual_delivery = None

        status = random.choices(
            DELIVERY_STATUSES,
            weights=[70, 15, 10, 5]
        )[0]

        if status == "Delivered":

            actual_delivery = estimated_delivery + timedelta(
                days=random.randint(-2, 3)
            )

        deliveries.append({
            "delivery_id": f"D{i:07d}",
            "order_id": order["order_id"],
            "carrier": random.choice(CARRIERS),
            "shipping_date": shipping_date,
            "estimated_delivery": estimated_delivery,
            "actual_delivery": actual_delivery,
            "delivery_status": status,
        })

    return pd.DataFrame(deliveries)


# SALVAR

def save_dataframe(df, filename):

    path = OUTPUT_DIR / filename

    df.to_csv(
        path,
        index=False,
        encoding="utf-8"
    )

    print(
        f"[OK] {filename}: "
        f"{len(df):,} registros"
    )


# MAIN

def main():

    print("=" * 60)
    print("MODERN DATA WAREHOUSE")
    print("GERAÇÃO DE DADOS")
    print("=" * 60)

    print("\nGerando customers...")
    customers = generate_customers()

    print("Gerando products...")
    products = generate_products()

    print("Gerando stores...")
    stores = generate_stores()

    print("Gerando sellers...")
    sellers = generate_sellers()

    print("Gerando orders...")
    orders = generate_orders(
        customers,
        sellers
    )

    print("Gerando order_items...")
    order_items = generate_order_items(
        orders,
        products
    )

    print("Gerando payments...")
    payments = generate_payments(
        orders,
        order_items
    )

    print("Gerando deliveries...")
    deliveries = generate_deliveries(
        orders
    )

    print("\nSalvando arquivos...\n")

    save_dataframe(
        customers,
        "customers.csv"
    )

    save_dataframe(
        products,
        "products.csv"
    )

    save_dataframe(
        stores,
        "stores.csv"
    )

    save_dataframe(
        sellers,
        "sellers.csv"
    )

    save_dataframe(
        orders,
        "orders.csv"
    )

    save_dataframe(
        order_items,
        "order_items.csv"
    )

    save_dataframe(
        payments,
        "payments.csv"
    )

    save_dataframe(
        deliveries,
        "deliveries.csv"
    )

    print("\n" + "=" * 60)
    print("GERAÇÃO FINALIZADA COM SUCESSO")
    print("=" * 60)


if __name__ == "__main__":
    main()
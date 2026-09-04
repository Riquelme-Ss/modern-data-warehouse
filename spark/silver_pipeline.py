# Codigos organizado por comentarios!

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    trim,
    lower
)


spark = (
    SparkSession.builder
    .appName("ModernDataWarehouse-Silver")
    .getOrCreate()
)


# CONFIGURAÇÕES

BRONZE_PATH = "s3a://data-lake/bronze"
SILVER_PATH = "s3a://data-lake/silver"


datasets = [
    "customers",
    "deliveries",
    "orders",
    "order_items",
    "payments",
    "products",
    "sellers",
    "stores"
]


# FUNÇÃO DE LIMPEZA

def clean_dataframe(df):

    # Remove linhas completamente vazias
    df = df.dropna(how="all")

    # Padroniza nomes das colunas
    for column in df.columns:

        new_name = (
            column
            .strip()
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
        )

        df = df.withColumnRenamed(column, new_name)

    # Remove espaços das colunas string
    for column, data_type in df.dtypes:

        if data_type == "string":

            df = df.withColumn(
                column,
                trim(col(column))
            )

    # Remove duplicidades
    df = df.dropDuplicates()

    return df


# PROCESSAMENTO

for dataset in datasets:

    print(f"\nProcessando: {dataset}")

    input_path = f"{BRONZE_PATH}/{dataset}/*.csv"
    output_path = f"{SILVER_PATH}/{dataset}"

    print(f"Lendo: {input_path}")

    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(input_path)
    )

    print("Schema original:")
    df.printSchema()

    print(f"Registros antes da limpeza: {df.count()}")

    df_clean = clean_dataframe(df)

    print(f"Registros depois da limpeza: {df_clean.count()}")

    (
        df_clean
        .write
        .mode("overwrite")
        .parquet(output_path)
    )

    print(f"Silver criada: {output_path}")


print("\n===================================")
print("PIPELINE BRONZE -> SILVER FINALIZADO")
print("===================================")


spark.stop()
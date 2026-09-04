
# Codigos organizados por comentarios


from pathlib import Path

from minio import Minio
from minio.error import S3Error


# CONFIGURAÇÕES

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "generated"

MINIO_HOST = "localhost:9000"
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "minioadmin"

BUCKET_NAME = "data-lake"


# CLIENTE MINIO

client = Minio(
    MINIO_HOST,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)


# DATASETS

DATASETS = [
    "customers",
    "products",
    "stores",
    "sellers",
    "orders",
    "order_items",
    "payments",
    "deliveries",
]


# CRIAR BUCKET

def create_bucket():

    if not client.bucket_exists(BUCKET_NAME):

        client.make_bucket(BUCKET_NAME)

        print(
            f"[OK] Bucket criado: {BUCKET_NAME}"
        )

    else:

        print(
            f"[OK] Bucket já existe: {BUCKET_NAME}"
        )


# UPLOAD

def upload_dataset(dataset):

    local_file = DATA_DIR / f"{dataset}.csv"

    object_name = (
        f"bronze/{dataset}/{dataset}.csv"
    )

    if not local_file.exists():

        print(
            f"[ERRO] Arquivo não encontrado: "
            f"{local_file}"
        )

        return

    client.fput_object(
        BUCKET_NAME,
        object_name,
        str(local_file),
        content_type="text/csv",
    )

    print(
        f"[OK] {dataset}.csv → "
        f"{object_name}"
    )


# MAIN

def main():

    print("=" * 60)
    print("DATA LAKE - BRONZE")
    print("=" * 60)

    try:

        create_bucket()

        print("\nEnviando datasets...\n")

        for dataset in DATASETS:

            upload_dataset(dataset)

        print("\n" + "=" * 60)
        print("INGESTÃO FINALIZADA COM SUCESSO")
        print("=" * 60)

    except S3Error as error:

        print(
            f"\n[ERRO MINIO] {error}"
        )


if __name__ == "__main__":
    main()
# Modern Data Warehouse

<p align="center">
  <strong>End-to-end Data Engineering Project</strong><br>
  Data Lake • Data Warehouse • ETL • Spark • dbt • Docker
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/dbt-FF694A?style=for-the-badge&logo=dbt&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</p>

---

## Sobre

Projeto completo de **Engenharia de Dados** construído para simular um ambiente moderno de dados, desde a ingestão até a camada analítica.

A arquitetura utiliza **Data Lake em MinIO**, processamento com **Apache Spark**, **Data Warehouse em PostgreSQL** e transformação/modelagem com **dbt**.

### Arquitetura

```text
                 DATA SOURCES
                      │
                      ▼
               ┌─────────────┐
               │    Python   │
               │  Ingestion  │
               └──────┬──────┘
                      │
                      ▼
              ┌───────────────┐
              │     MinIO     │
              │   Data Lake   │
              └───────┬───────┘
                      │
                ┌─────▼─────┐
                │   Bronze  │
                └─────┬─────┘
                      │
                Apache Spark
                      │
                ┌─────▼─────┐
                │   Silver  │
                └─────┬─────┘
                      │
                ┌─────▼─────┐
                │    Gold   │
                └─────┬─────┘
                      │
                      ▼
             ┌────────────────┐
             │   PostgreSQL   │
             │ Data Warehouse │
             └───────┬────────┘
                     │
                     ▼
                  ┌─────┐
                  │ dbt │
                  └──┬──┘
                     │
                     ▼
                 Power BI
```

---

## Stack

**Data Engineering**

* Python
* Pandas
* Apache Spark
* MinIO / S3
* Parquet

**Data Warehouse**

* PostgreSQL
* Star Schema
* Fact & Dimension Tables

**Analytics Engineering**

* dbt
* SQL
* Data Quality
* Data Lineage

**Infrastructure**

* Docker
* Docker Compose
* Git / GitHub

---

## Data

|                |                         |
| -------------- | ----------------------: |
| Clientes       |              **50.000** |
| Produtos       |               **5.000** |
| Vendedores     |               **1.000** |
| Itens de venda |           **1.499.327** |
| Categorias     |                  **10** |
| Período        | **Ago/2024 → Ago/2026** |

---

## dbt

**9 modelos · 6 fontes · 35 testes**

### Marts

`mart_sales_monthly`
Indicadores de vendas por mês.

`mart_sales_by_category`
Performance por categoria.

`mart_customer_360`
Visão consolidada dos clientes.

### Data Quality

```text
35 / 35 tests passed
0 errors
0 warnings
```

Incluindo validação de consistência financeira entre:

`gross_amount - discount_amount = net_amount`

---

## Estrutura

```text
modern-data-warehouse/
│
├── ingestion/
│   ├── generate_data.py
│   └── upload_to_minio.py
│
├── spark/
│   ├── Dockerfile
│   └── silver_pipeline.py
│
├── dbt/
│   ├── models/
│   └── tests/
│
├── docker/
│   └── spark/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Executar

```bash
git clone https://github.com/Riquelme-Ss/modern-data-warehouse.git

cd modern-data-warehouse

docker compose up -d --build
```

Executar dbt:

```bash
docker compose run --rm dbt run --profiles-dir .
```

Testes:

```bash
docker compose run --rm dbt test --profiles-dir .
```

Documentação:

```bash
docker compose run --rm dbt docs generate --profiles-dir .
```

---

## Status

| Componente             | Status |
| ---------------------- | :----: |
| Data Ingestion         |    ✅   |
| Data Lake              |    ✅   |
| Bronze / Silver / Gold |    ✅   |
| Apache Spark           |    ✅   |
| PostgreSQL DW          |    ✅   |
| Dimensional Modeling   |    ✅   |
| dbt                    |    ✅   |
| Data Quality           |    ✅   |
| Data Lineage           |    ✅   |
| Docker                 |    ✅   |
| GitHub                 |    ✅   |
| Power BI               |   🔄   |
| Airflow                |   🔜   |
| CI/CD                  |   🔜   |

---

## Autor

**Pablo Riquelme**

[LinkedIn](https://www.linkedin.com/in/pablo-riquelme-ss/) · [GitHub](https://github.com/Riquelme-Ss)

**Engenharia de Dados · Data Engineering**

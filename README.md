# Modern Data Warehouse

### Um sistema que transforma milhões de linhas de dados bagunçados em respostas claras para o negócio.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694A?style=for-the-badge&logo=dbt&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## Em 30 segundos

Imagine uma rede de lojas que registra **1,5 milhão de vendas** em planilhas e sistemas diferentes.
A diretoria quer saber: *quanto vendemos por mês? Qual categoria vai melhor? Quem são os melhores clientes?*

Responder isso direto dos dados brutos é lento e sujeito a erro.

Este projeto constrói o caminho completo entre o dado bruto e a resposta:

1. **Gera** os dados de vendas
2. **Guarda** tudo em um depósito central
3. **Limpa e organiza** os dados em etapas
4. **Monta** um banco de dados pronto para consulta
5. **Testa** automaticamente se os números estão corretos

> Os dados são **fictícios**, gerados por este projeto para simular uma operação de varejo.
> Nenhuma informação real de pessoas ou empresas foi usada.

---

## O que este projeto entrega

| Pergunta de negócio | Onde está a resposta |
| ------------------- | -------------------- |
| Quanto vendemos em cada mês? | `mart_sales_monthly` |
| Quais categorias de produto vendem melhor? | `mart_sales_by_category` |
| Como é o perfil de cada cliente? | `mart_customer_360` |

Esses três "marts" são tabelas prontas para alimentar relatórios e dashboards.

**Garantia de qualidade:** o projeto roda **35 testes automáticos** nos dados, e todos passam. Um deles confirma que a conta financeira fecha em todas as vendas:

```
valor bruto - desconto = valor líquido
```

---

## Como funciona (sem jargão)

Pense numa **cozinha profissional**:

| Etapa | Na cozinha | No projeto |
| ----- | ---------- | ---------- |
| Ingestão | Chegada dos ingredientes | Scripts em Python geram os dados e enviam ao depósito |
| Data Lake (MinIO) | A despensa | Armazena tudo, do jeito que chegou |
| Bronze | Ingredientes crus | Dado bruto, sem alteração |
| Silver | Ingredientes lavados e cortados | Dado limpo e padronizado pelo Apache Spark |
| Gold | Prato pronto | Dado organizado para responder perguntas |
| PostgreSQL | O balcão de pedidos | Banco de dados onde as consultas acontecem |
| dbt | O controle de qualidade | Cria as tabelas finais e testa os resultados |
| Power BI | O cardápio apresentado ao cliente | Dashboard final (em desenvolvimento) |

### Visão geral do fluxo

```
Dados gerados (Python)
        │
        ▼
 Depósito central (MinIO)
        │
        ▼
 Bronze (bruto) → Silver (limpo) → Gold (pronto)     ← processado pelo Spark
        │
        ▼
 Banco de dados (PostgreSQL)
        │
        ▼
 Tabelas finais e testes (dbt)
        │
        ▼
 Dashboard (Power BI, em desenvolvimento)
```

---

## Números do projeto

| O que | Quantidade |
| ----- | ---------- |
| Clientes | 50.000 |
| Produtos | 5.000 |
| Vendedores | 1.000 |
| Itens de venda | 1.499.327 |
| Categorias | 10 |
| Período simulado | Agosto/2024 a Agosto/2026 |
| Modelos dbt | 9 |
| Testes automáticos | 35 (todos aprovados) |

---

## Por que essas escolhas?

- **Camadas (Bronze, Silver, Gold):** se algo der errado, dá para refazer a partir da etapa anterior sem perder o dado original.
- **Spark:** processa volumes grandes de forma rápida.
- **MinIO:** funciona como a nuvem da Amazon (S3), mas roda no computador, sem custo. O projeto poderia migrar para a nuvem sem reescrever o código.
- **dbt:** deixa as regras de negócio escritas em SQL, versionadas e testadas.
- **Docker:** quem baixar o projeto sobe o ambiente inteiro com poucos comandos, sem instalar cada ferramenta na mão.

---

## Situação atual

| Componente | Status |
| ---------- | :----: |
| Geração e ingestão de dados | ✅ |
| Data Lake (MinIO) | ✅ |
| Camadas Bronze, Silver e Gold | ✅ |
| Processamento com Spark | ✅ |
| Banco de dados PostgreSQL | ✅ |
| Modelagem dimensional | ✅ |
| dbt e testes de qualidade | ✅ |
| Docker | ✅ |
| Dashboard no Power BI | 🔄 Em andamento |
| Automação com Airflow | 🔜 Planejado |
| Testes automáticos no GitHub (CI/CD) | 🔜 Planejado |

---

# Para quem quer rodar ou avaliar o código

## Tecnologias

| Área | Ferramentas |
| ---- | ----------- |
| Engenharia de dados | Python, Pandas, Apache Spark, MinIO (S3), Parquet |
| Data Warehouse | PostgreSQL, Star Schema, tabelas fato e dimensão |
| Analytics engineering | dbt, SQL, testes de dados, lineage |
| Infraestrutura | Docker, Docker Compose, Git/GitHub |

## Serviços do Docker Compose

| Serviço | Imagem | Portas | Função |
| ------- | ------ | ------ | ------ |
| MinIO | `minio/minio` | 9000 (API), 9001 (console) | Data Lake compatível com S3 |
| PostgreSQL | `postgres:16` | 5432 | Data Warehouse |
| Spark | build local (3.5.6) | 8080 (UI), 7077 | Processamento Bronze → Silver → Gold |
| dbt | `dbt-postgres:1.6` | 8081 | Modelagem, testes e documentação |

## Estrutura do projeto

```
modern-data-warehouse/
├── ingestion/
│   ├── generate_data.py      # gera os dados fictícios
│   └── upload_to_minio.py    # envia os dados para o Data Lake
├── spark/
│   └── silver_pipeline.py    # processamento com Spark
├── dbt/
│   ├── models/               # modelos e marts
│   └── tests/                # testes de qualidade
├── docker/
│   └── spark/                # Dockerfile do Spark
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

## Pré-requisitos

- Docker e Docker Compose
- Git
- Python 3.10 ou superior (para os scripts de ingestão)

## Passo a passo para rodar

**1. Baixar o projeto e configurar as senhas**

```bash
git clone https://github.com/Riquelme-Ss/modern-data-warehouse.git
cd modern-data-warehouse

cp .env.example .env
```

Abra o arquivo `.env` e defina as credenciais: `MINIO_ROOT_USER`, `MINIO_ROOT_PASSWORD`,
`POSTGRES_DB`, `POSTGRES_USER` e `POSTGRES_PASSWORD`.
A senha do MinIO precisa ter pelo menos 8 caracteres.

**2. Subir os serviços**

```bash
docker compose up -d --build
```

**3. Gerar os dados e enviar ao Data Lake**

```bash
python -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements.txt

python ingestion/generate_data.py
python ingestion/upload_to_minio.py
```

**4. Processar com Spark**

```bash
docker compose exec spark /opt/spark/bin/spark-submit \
  --master local[*] \
  /opt/spark/work/silver_pipeline.py
```

**5. Criar as tabelas finais e rodar os testes**

```bash
docker compose run --rm dbt run --profiles-dir .
docker compose run --rm dbt test --profiles-dir .
```

**6. Gerar a documentação (opcional)**

```bash
docker compose run --rm dbt docs generate --profiles-dir .
docker compose run --rm --service-ports dbt docs serve --profiles-dir . --port 8081
```

### Onde ver o resultado

| O quê | Endereço |
| ----- | -------- |
| Console do MinIO (arquivos do Data Lake) | http://localhost:9001 |
| Spark UI | http://localhost:8080 |
| Documentação do dbt | http://localhost:8081 |
| PostgreSQL | `localhost:5432` |

### Para encerrar

```bash
docker compose down        # desliga e mantém os dados
docker compose down -v     # desliga e apaga os dados
```

## Mapa do fluxo de dados (lineage)

![Lineage do dbt](docs/dbt_lineage.png)

## Glossário

| Termo | Significado simples |
| ----- | ------------------- |
| ETL | Extrair, transformar e carregar dados |
| Data Lake | Depósito que guarda dados de todo tipo, em estado bruto |
| Data Warehouse | Banco de dados organizado para análises e relatórios |
| Spark | Ferramenta que processa grandes volumes de dados com rapidez |
| dbt | Ferramenta que cria e testa tabelas usando SQL |
| Star Schema | Forma de organizar tabelas: uma central (fatos) cercada por tabelas de apoio (dimensões) |
| Mart | Tabela final, pronta para responder uma pergunta de negócio |
| Lineage | Mapa que mostra de onde cada dado veio |
| Docker | Ferramenta que empacota um sistema para rodar igual em qualquer computador |

## Próximos passos

- [ ] Dashboard no Power BI usando `mart_sales_monthly`
- [ ] Automação do pipeline com Airflow
- [ ] Testes automáticos no GitHub Actions
- [ ] Carga incremental, processando só os dados novos

## Autor

**Pablo Riquelme**, Engenharia de Dados

[LinkedIn](https://www.linkedin.com/in/pablo-riquelme-santana-de-souza-226671225) · [GitHub](https://github.com/Riquelme-Ss)

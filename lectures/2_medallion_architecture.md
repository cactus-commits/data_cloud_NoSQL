## Medallion architecture 

### What is medallion architecture
- a way to organize data in data lakehouse
- when data i continously refined throughout a data pipeline, data with imporving quality are stored in different layers (bronze, silver, gold)

## Benefits
- preserve historical archive of sta and make reprocessing easy 
- enable step-by-step transformation
- data lineage for debugging

## Data layers
This image shows an overview of the medallion architecture. 

> [!NOTE]
> All data is stil in the unity catalog but you can have the different layers as different schemas.

<img src="https://github.com/kokchun/assets/blob/main/databricks/medallion_architecture_overview.png?raw=true" alt="intro to cloud computing" width="600">


> [!NOTE]
>  a common misconception about the medallion architecture is that it must compose of these three layers. In reality it should be much more flexible than that and should adapt to your specific business needs. It could for example just be two layers, or could be more than 3 layers.

<!-- 
### Folder structure

```md
silver/
├── fact_orders
├── dim_customers
└── dim_products

gold/
├── daily_sales_report
└── customer_summary
```

## Spark declarative pipelines 

## ETL pipelines in databricks -->


## Read more 👓
[What is medallion architecture?](https://www.databricks.com/blog/what-is-medallion-architecture) <br>


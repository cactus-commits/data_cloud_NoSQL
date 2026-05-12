from pyspark import pipelines as dp 

# Vår base directory/base volume
BASE_DIR = "/Volumes/supply_chain_demo/default/raw"

# Vi läser in i en spark dataframe
schema = spark.read.format("csv").options(header=True, inferSchema=True).load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv").schema # Vi behöver schema för att kunna skapa en tabell

# Decorator 
@dp.table(
  name="supply_chain_demo.bronze.raw_supply_chain", 
  comment = "Raw supply chain data for company X",
  table_properties={"delta.columnMapping.mode": "name"}
  ) # raw_supply_chain is the name of the table


# När man har en Decorator behöver man dekorera en function
# 1. Vi returnerar en tabell, 2. men vi behöver läsa in den med load
def raw_supply_chain():
  return spark.readStream.format("csv").options(header="true", encoding="UTF-8").schema(schema).load(f"{BASE_DIR}/data")

  
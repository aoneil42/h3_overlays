import geopandas as gpd

h3_0 = gpd.read_parquet('h3_0.parquet')
lsib = gpd.read_parquet('lsib.parquet')

lsibhex = gpd.overlay(lsib, h3_0, 'union', False, True)

lsibhex.to_parquet('lsibhex.parquet')

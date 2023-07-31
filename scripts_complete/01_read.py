# %%
import polars as pl
# %%
# it will default to only reading in two columns as the first row has meta information in two cells.
dat_try = pl.read_csv("../data/API_Download_DS2_en_csv_v2_5657328.csv")
dat_try
# %%
# now we get the data read in.  However, it isn't handling the column types correctly
dat_try = pl.read_csv("../data/API_Download_DS2_en_csv_v2_5657328.csv", skip_rows=4)
dat_try
# %%
# Notice that the world health leaves missing as blanks in the csv. We need to explain that blanks aren't strings but missing values.
dat = pl.read_csv("../data/API_Download_DS2_en_csv_v2_5657328.csv", skip_rows=4, null_values = "")
dat
# %%
# We don't like the World Banks wide format.  Let's clean it upt to long format.
dat_long = dat.melt(id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"])

# %%
dat_long.write_csv("../data/long.csv")
dat_long.write_parquet("../data/long.parquet")

# %%
print(dat_long.estimated_size("mb"))
dat_long.select(pl.count("value"))

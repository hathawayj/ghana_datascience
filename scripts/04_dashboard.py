# %%
# packages
import streamlit as st
import polars as pl
import plotly.express as px
import plotly.io as pio
pio.templates.default = "simple_white"
# %%
# Data: make sure have our created files.
# dat = pl.read_parquet("data/dat_munged.parquet")
# info = pl.read_csv("data/Metadata_Indicator_API_Download_DS2_en_csv_v2_5657328.csv").rename({"INDICATOR_CODE":"Indicator Code", "INDICATOR_NAME":"Indicator Name"})
# dat_vars = pl.read_parquet("data/dat_vars.parquet")

# %%
# Example Chart
# drop_country =  ["ZAF"]
# indicator_code = "NY.GDP.PCAP.PP.KD"
# list_name = dat_vars.select("Indicator Name").to_series().to_list()
# list_code = dat_vars.select("Indicator Code").to_series().to_list()
list_country_code = ["ZAF", "ZWE", "KEN", "NGA", "GHA", "COD"]
list_country_name = ["South Africa", "Zimbabwe", "Kenya", "Nigeria", "Ghana", "Congo, Dem. Rep."]


drop_country = st.sidebar.multiselect("Remove Country (Country Code)", list_country_code)

checked_var = st.sidebar.checkbox("Use Variable Name")
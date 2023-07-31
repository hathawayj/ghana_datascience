# %%
import polars as pl
import plotly.express as px
import plotly.io as pio
pio.templates.default = "simple_white"
# ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

# %%
# read data
# pl.read_parquet(), pl.read_csv(), .rename(new_names)
new_names = {"INDICATOR_CODE":"Indicator Code", "INDICATOR_NAME":"Indicator Name"}

dat = pl.read_parquet("../data/dat_munged.parquet")
info = pl.read_csv("../data/Metadata_Indicator_API_Download_DS2_en_csv_v2_5657328.csv").rename()


# %%
# Now let's build an indicator variable summary table and save it to data/dat_vars.parquet
# .groupby(), .count(), .pivot(), .with_columns(), pl.col(), .fill_null(), .alias(), .sort(descending=False), write_parquet()


# %%
# Let's build a scatter plot of one of the variables
# px.line(), .filter(() & ()), .is_in(), .is_not_null()

# %%
# Can we automate our chart so that once we pick a variable the chart information updates?
# .select(), .to_series()[0], text_string[], test_string.find("(")+1:text_string.find(")")
# px.line(labels = {dictionary})


# %%
# some setup for our next chart
drop_country = ["ZAF"]
# 0 is color, 1 is size, 2 is y axis
plot_codes = ["IT.NET.USER.ZS", "EG.CFT.ACCS.ZS", "NY.GDP.PCAP.PP.KD"]
text_table = info.filter(pl.col("Indicator Code").is_in(plot_codes))\
    .select("Indicator Code","SOURCE_NOTE")\
    .join(dat_vars, on=["Indicator Code"])\
    .with_columns([
        pl.col("SOURCE_NOTE").str.slice(0,200).alias("SOURCE_NOTE"),
        (pl.col("Indicator Name")  + "<br><sup>" + pl.col("SOURCE_NOTE") + "</sup>").alias("chart_title")
        ])

new_labels =dict(zip(text_table["Indicator Code"], text_table["Indicator Name"]))
# %%
# can we pivot our long format data to wide format using the plot_codes above?
# lets only use the years 2006 - 2021
# .filter(), pl.col(), .is_in(), .select(), .pivot(),


# %%
# Now let's put this data into a bubble chart
# px.scatter()
# color=plot_codes[0], size=plot_codes[1],  facet_col="Country Code", labels = new_labels, color_continuous_scale="Sunsetdark"

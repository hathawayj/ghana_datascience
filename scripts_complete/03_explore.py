# %%
import polars as pl
import plotly.express as px
import plotly.io as pio
pio.templates.default = "simple_white"
# ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]

dat = pl.read_parquet("../data/dat_munged.parquet")
info = pl.read_csv("../data/Metadata_Indicator_API_Download_DS2_en_csv_v2_5657328.csv").rename({"INDICATOR_CODE":"Indicator Code", "INDICATOR_NAME":"Indicator Name"})

dat_vars = dat.filter(pl.col("value").is_null())\
    .groupby("Indicator Name", "Indicator Code", "Country Code").count()\
    .pivot(values="count", index=["Indicator Name", "Indicator Code"], columns="Country Code", aggregate_function="first")\
    .with_columns((pl.col("COD").fill_null(0) + pl.col("GHA").fill_null(0) +
                   pl.col("KEN").fill_null(0) + pl.col("NGA").fill_null(0) +
                   pl.col("ZAF").fill_null(0) + pl.col("ZWE").fill_null(0)).alias("total"))\
    .sort(pl.col("total"), descending=False)

dat_vars.write_parquet("../data/dat_vars.parquet")

dat_vars
# %%
# Access to fuels
# Access to internet
# GDP

drop_country =  ["ZAF"]
indicator_code = "NY.GDP.PCAP.PP.KD"
title_text = dat_vars.filter(pl.col("Indicator Code") == indicator_code).select("Indicator Name").to_series()[0]
subtitle_text = info.filter(pl.col("Indicator Code") == indicator_code).select("SOURCE_NOTE").to_series()[0]
subtitle_text = subtitle_text[1:200]
chart_title = title_text + "<br><sup>" + subtitle_text + "</sup>"
y_axis_title = chart_title[chart_title.find("(")+1:chart_title.find(")")]
chart_dat = dat.filter((pl.col("Indicator Code").is_in([indicator_code])) & (~pl.col("Country Code").is_in(drop_country)) & (pl.col("value").is_not_null()))
sp = px.line(chart_dat,
    x="year", y="value", color="Country Code", markers=True,
    labels = {"year":"Year", "value":y_axis_title},
    title = chart_title)
sp
# %%
# https://2001-2009.state.gov/r/pa/ho/time/pcw/98678.htm#:~:text=Apartheid%2C%20the%20Afrikaans%20name%20given,a%20democratic%20government%20in%201994.
# What happened in South Africa in the 1990s?
# What happened in Nigeria in early 2000?
# What happened in Ghana in 2010s?
# sp.add_annotation(
#         x=1994, y=4100,
#         text="Democratic Government",
#         showarrow=True,
#         yshift=10)
# %%
# try a ternary plot to look at three variables
# We have to format the data a bit different for this chart.
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



dat_wide = dat.filter(
        (pl.col("Indicator Code").is_in(plot_codes)) &
        (pl.col("year") > 2005) &
        (pl.col("year") < 2022))\
    .select("Country Code", "Indicator Code", "year", "value")\
    .pivot(values="value", index=["Country Code", "year"], columns="Indicator Code", aggregate_function="first")
dat_wide

fig = px.scatter(dat_wide.filter(~pl.col("Country Code").is_in(drop_country)),
    x="year", y=plot_codes[2],
    color=plot_codes[0], size=plot_codes[1],  facet_col="Country Code",
     labels = new_labels, color_continuous_scale="Sunsetdark")
fig.show()

# %%
#map
# %%
# two variables with time
# https://plotly.com/python/line-charts/
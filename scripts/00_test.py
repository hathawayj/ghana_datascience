# %%
import streamlit as st
import polars as pl
import plotly.express as px
import plotly.io as pio
pio.templates.default = "simple_white"

# %%
dat = pl.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
dat
# %%
fig = px.scatter(dat, x="first column", y="second column")
fig
# %%
st.markdown("## Hello")
# %%
# now open your Terminal and run
# streamlit run scripts/00_test.py
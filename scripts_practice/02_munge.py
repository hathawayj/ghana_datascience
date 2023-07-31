# %%
import polars as pl
dat_long = pl.read_parquet("../data/long.parquet")
dat_long


# %%
# now we need to fix the year column and give it a better name.
# .with_column, pl.col(), .cast(), .alias(), .rename(), pl.Int64
dat_long = dat_long # finish out the code

# %%
# Can we split out the information in the indicator Code into their own columns
# split string: example VC.IDP.TOCV into list object ["VC", "IDP", "TOCV"]
# convert to struct object {"VC","IDP","TOCV",null,null,null,null}
# .select(), pl.col(), .str.split(), .arr.to_struct()

indicator_columns = dat_long # finish out the code


# %%
# now display the difference
dat_long.select(pl.col("Indicator Code"))
indicator_columns

# %%
# Let's create a table with our five values as five columns.
# .unnest()
dat_columns = indicator_columns # finish out the code

# %%
# What should we call these columns?
# https://datahelpdesk.worldbank.org/knowledgebase/articles/201175-how-does-the-world-bank-code-its-indicators or readme.md in this folder
# .rename()

# %%
# Let's combine our indicator columns with our dat_long data and then reorder the columns.
# .collumns, .hstack(), .select()

names = dat_final.columns
print(names)
# how do we want to order the columns
new_order = [1, 2]
# This is a list comprehension.  A succint for loop
name_order = [names[i] for i in new_order]

# %%
# now we can write our data to file `dat_munged.csv` and `dat_munged.parquet`
# .write_parquet() and .write_csv()

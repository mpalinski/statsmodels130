#!/usr/bin/env python
# coding: utf-8

# DO NOT EDIT
# Autogenerated from the notebook tsa_dates.ipynb.
# Edit the notebook and then sync the output with this file.
#
# flake8: noqa
# DO NOT EDIT

# # Dates in timeseries models

import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg, ar_select_order

plt.rc("figure", figsize=(16, 8))
plt.rc("font", size=14)

# ## Getting started

data = sm.datasets.sunspots.load()

# Right now an annual date series must be datetimes at the end of the
# year.

from datetime import datetime

dates = pd.date_range("1700-1-1", periods=len(data.endog), freq="A-DEC")

# ## Using Pandas
#
# Make a pandas TimeSeries or DataFrame

data.endog.index = dates
endog = data.endog
endog

# Instantiate the model

selection_res = ar_select_order(endog,
                                9,
                                old_names=False,
                                seasonal=True,
                                period=11)
pandas_ar_res = selection_res.model.fit()

# Out-of-sample prediction

pred = pandas_ar_res.predict(start="2005", end="2027")
print(pred)

fig = pandas_ar_res.plot_predict(start="2005", end="2027")
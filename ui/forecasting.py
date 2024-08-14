import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from sktime.datasets import load_airline
from sktime.forecasting.naive import NaiveForecaster


def forecasting_page():
    """Some docstring."""
    y = load_airline()
    data = y.reset_index()
    data["Period"] = [i.to_timestamp() for i in data["Period"]]
    data["type"] = "historical"

    # step 2: specifying forecasting horizon
    fh = np.arange(1, 37)
    # step 3: specifying the forecasting algorithm
    forecaster = NaiveForecaster(strategy="last", sp=12)
    # step 4: fitting the forecaster
    forecaster.fit(y)
    # step 5: querying predictions
    y_pred = forecaster.predict(fh)
    preds = y_pred.reset_index()
    preds["index"] = [i.to_timestamp() for i in preds["index"]]
    preds = preds.rename(columns={"index": "Period"})
    preds["type"] = "forecast"

    asd = pd.concat([data, preds])

    line = alt.Chart(asd).mark_line(point=True).encode(x="Period", y="Number of airline passengers", color="type")

    st.altair_chart(line, use_container_width=True)


forecasting_page()

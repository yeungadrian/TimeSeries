import altair as alt
import streamlit as st
from sktime.datasets import load_airline, load_macroeconomic


def datasets_page():
    """Some docstrings."""
    available_datasets = {"airlines": load_airline, "macroeconomic": load_macroeconomic}

    st.title("Explore datasets")
    selected_dataset = st.sidebar.selectbox("Select dataset", available_datasets.keys())
    dataset = available_datasets[selected_dataset]()
    dataset = dataset.reset_index()
    dataset["Period"] = [i.to_timestamp() for i in dataset["Period"]]

    features = [i for i in dataset.columns if i != "Period"]
    selected_feature = st.sidebar.multiselect("Select feature", features, default=features[0])

    if len(selected_feature) > 1:
        pass

    line = alt.Chart(dataset).mark_line(point=True).encode(x="Period", y=selected_feature[0])

    st.altair_chart(line, use_container_width=True)


datasets_page()

import streamlit as st

st.set_page_config(page_title="Time Series", page_icon="📊", layout="wide")

dashboard = st.Page("ui/datasets.py", title="Datasets", icon=":material/manage_search:", default=True)
forecasting = st.Page("ui/forecasting.py", title="Forecasting", icon=":material/monitoring:")


pg = st.navigation(
    {
        "Time Series": [dashboard, forecasting],
    }
)


if __name__ == "__main__":
    pg.run()

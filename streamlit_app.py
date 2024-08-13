import streamlit as st

st.set_page_config(page_title="Time Series", page_icon="📊", layout="wide")

dashboard = st.Page("pages/datasets.py", title="Datasets", icon=":material/dashboard:", default=True)
forecasting = st.Page("pages/forecasting.py", title="Forecasting", icon=":material/bug_report:")
probabilistic = st.Page(
    "pages/probabilistic.py", title="Probabilistic Forecasting", icon=":material/notification_important:"
)


pg = st.navigation(
    {
        "Time Series": [dashboard, forecasting, probabilistic],
    }
)


if __name__ == "__main__":
    pg.run()

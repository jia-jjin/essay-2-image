import streamlit as st
import pandas as pd

@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

df = get_UN_data()
countries = st.multiselect(
    "Choose countries", list(df.index), ["China", "United States of America"]
)
if not countries:
    st.error("Please select at least one country.")
else:
    data = df.loc[countries]
    data /= 1000000.0
    st.write("### Gross Agricultural Production ($B)", data.sort_index())

    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
    )
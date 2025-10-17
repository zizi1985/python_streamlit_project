import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

@st.cache_data
def load_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)

def upload_csv():
    st.write("upload csv")

    uploaded_file = st.file_uploader("📁 choose file:", type=["xlsx", "xls", "csv"])

    if uploaded_file:
        try:
            df = load_file(uploaded_file)
        except Exception as e:
            st.error(f"❌ Exception in reading file: {e}")
            return
        else:
            st.success("✅ Upload was successful")

            gb = GridOptionsBuilder.from_dataframe(df)

            gb.configure_pagination(
                enabled=True, paginationAutoPageSize=False, paginationPageSize=10
            )
            gb.configure_default_column(
                sortable=True,
                filter=True,
                resizable=True,
            )
            gb.configure_grid_options(domLayout='normal')

            grid_options = gb.build()

            st.write("📊 File data:")
            AgGrid(
                df,
                gridOptions=grid_options,
                update_mode=GridUpdateMode.NO_UPDATE,
                enable_enterprise_modules=False,
                theme="streamlit",
                height=400,
                fit_columns_on_grid_load=True,
            )
    else:
        st.info("Please upload a csv file")



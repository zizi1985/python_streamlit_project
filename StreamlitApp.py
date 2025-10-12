
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


st.set_page_config(page_title="Sample Streamlit App")
st.title("Streamlit App")


page = st.sidebar.radio("Choose an option",( "📝 Form","📂️ CSV Uploader", "🎑 Image Gallery"))
if page == "📝 Form":
    st.title("📝 User Information form")

    with st.form("user_info_form", clear_on_submit=False):
        name = st.text_input("👤 Enter your name")
        age = st.number_input("🎂 Enter your age", min_value=0, max_value=120, step=1)
        feedback = st.text_area("🗒️ Your Feedback", placeholder="plz write about your feedback.")
        acceptance = st.checkbox("✅ I accept the terms and conditions")
        gender = st.radio("🚻 Gender", ["👩Female", "🧑Male", "Other"])
        work_days = st.slider("How many days you work per week?",min_value=0,max_value=7, step=1)

        submitted = st.form_submit_button("submit")

        if submitted:
            if not name or not age or not feedback:
                st.warning("please fill all fields")
            else:
                st.success(f"Thank you for submitting {name}.🎉")
                st.write("**Registered data:**")
                st.write(f"- name: {name}")
                st.write(f"- age: {age}")
                st.write(f"- feedback: {feedback}")
                st.write(f"- ok: {acceptance}")
                st.write(f"- gender: {gender}")


elif page == "📂️ CSV Uploader":
    st.title("📂 CSV Uploader & Interactive Table")

    st.write("upload csv")

    uploaded_file = st.file_uploader("📁 choose file:", type=["xlsx", "xls", "csv"])

    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"❌ Exception in reading file: {e}")
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

elif page == "🎑 Image Gallery":
    st.title("🎑 Image Gallery With Batch Uploader")

    uploaded_images = st.file_uploader(
        "📁 Upload image:",
        type=["png", "jpg", "jpeg", "gif"],
        accept_multiple_files=True
    )

    if uploaded_images:
        st.success(f"✅ {len(uploaded_images)} selected images!")

        cols = st.columns(3)
        for i, image_file in enumerate(uploaded_images):
            with cols[i % 3]:
                st.image(image_file, caption=image_file.name, use_container_width=True)
    else:
        st.info("Please upload new images.")

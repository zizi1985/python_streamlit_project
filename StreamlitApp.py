
import streamlit as st


st.set_page_config(page_title="Sample Streamlit App")
st.title("Streamlit App")

page = st.sidebar.radio("Choose an option",( "📝 Form","📂️ CSV Uploader", "🎑 Image Gallery"))


if page == "📝 Form":
    st.title("📝 User Information form")
    from FormPage import form
    form()

elif page == "📂️ CSV Uploader":
    st.title("📂 CSV Uploader & Interactive Table")
    from CsvUploaderPage import upload_csv
    upload_csv()

elif page == "🎑 Image Gallery":
    st.title("🎑 Image Gallery With Batch Uploader")
    from ImageGalleryPage import image_gallery
    image_gallery()

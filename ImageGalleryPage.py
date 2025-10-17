import streamlit as st


def image_gallery():
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

import streamlit as st

def form():

 with st.form("user_info_form", clear_on_submit=False):
    name = st.text_input("👤 Enter your name")
    age = st.number_input("🎂 Enter your age", min_value=0, max_value=120, step=1)
    feedback = st.text_area("🗒️ Your Feedback", placeholder="plz write about your feedback.")
    acceptance = st.checkbox("✅ I accept the terms and conditions")
    gender = st.radio("🚻 Gender", ["👩Female", "🧑Male", "Other"])
    work_days = st.slider("How many days you work per week?", min_value=0, max_value=7, step=1)

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
            st.write(f"- workDays: {work_days}")


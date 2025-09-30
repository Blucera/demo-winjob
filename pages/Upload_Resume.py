import streamlit as st
from uuid import uuid4

from core import is_domain_allowed
from core.embedding_model import EmbeddingManager
from core.resumeManager import ResumeManager

resp = is_domain_allowed()
if not resp[0]:
    st.error("This app is not allowed on this domain.")
    st.stop()

st.set_page_config(page_title="Upload Resume", layout="centered")

st.header("Upload Your Resume")
st.caption("Submit your resume to get personalized job matches!")

message_container = st.container()

# ---- RESUME UPLOAD SECTION ----
resume = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
if resume:
    rm = ResumeManager(resume)
    try:
        text = rm.get_text()

        if st.button("Submit Resume"):
            if not resume:
                message_container.error("Please upload a resume file before submitting.")
            else:

                rm.save_resume()

                # ---- DOCUMENT PROCESSING
                message_container.success("Resume uploaded successfully!")
                message_container.info("Go to **Suggested Jobs** page to see job matches.")

    except Exception as e:
        message_container.error("Invalid File Type! Please upload PDF, Docx or TXT")
        resume = None

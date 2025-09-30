import streamlit as st
import pandas as pd

from core import is_domain_allowed
from core.job_manager import JobManager

resp = is_domain_allowed()
if not resp[0]:
    st.error("This app is not allowed on this domain.")
    st.stop()

st.set_page_config(page_title="All Jobs", layout="wide")

st.header("Browse Jobs")
st.caption("Find the perfect job with WinJob extensive database!")

# ---- SETTING JOB MANAGER AND GETTING ALL JOBS
job_manager = JobManager()
all_jobs = pd.DataFrame(job_manager.get_all_jobs())

# ---- DISPLAYING ALL JOBS IN TABLE
if not all_jobs.empty:
    # Add links to job detail page with query param
    all_jobs["view"] = [f"/Job_Details?job_id={job['id']}" for _, job in all_jobs.iterrows()]

    st.data_editor(
        all_jobs,
        width="stretch",
        column_order=["title", "description", "salary", "type", "posted_date", "view"],
        hide_index=True,
        column_config={
            "title": "Job Title",
            "description": "Job Description",
            "salary": st.column_config.NumberColumn("Salary", format="$%.2f"),
            "type": "Work Type",
            "posted_date": "Posted On",
            "view": st.column_config.LinkColumn("Action", display_text="View")
        },
        disabled=["title", "description", "salary", "type", "posted_date"]
    )
else:
    st.info("No Jobs available right now!")

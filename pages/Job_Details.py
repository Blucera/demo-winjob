import streamlit as st

from core import is_domain_allowed
from core.job_manager import JobManager

resp = is_domain_allowed()
if not resp[0]:
    st.error("This app is not allowed on this domain.")
    st.stop()

st.set_page_config(page_title="Job Details", layout="wide")

job_manager = JobManager()

# Read job_id from URL query params
query_params = st.query_params
job_id = query_params.get("job_id")

if job_id:
    job = job_manager.get_job(job_id)
    if job:
        st.header(job["title"])
        st.caption(f"Posted on {job['posted_date']} | {job['job_type']} | Salary: ${job['salary']:.2f}")
        st.markdown("### Description")
        st.write(job["description"])
    else:
        st.error("Job not found!")
else:
    st.error("No job selected!")

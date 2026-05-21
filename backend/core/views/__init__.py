from .dashboard_views import dashboard

# candidate logic 
from .candidate_views import (
    candidates_list,
    add_candidate,
    candidate_details,
    edit_candidate,
    delete_candidate,
)
# company logic
from .company_views import (
    companies_list,
    add_company,
    company_details,
    edit_company,
    delete_company,
)
# job logic
from .job_views import (
    jobs_list,
    add_job,
    job_details,
    edit_job,
    delete_job,
)
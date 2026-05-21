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
#applications logic
from .application_views import (
    applications_list,
    add_application,
    application_details,
    edit_application,
    delete_application,
)
# interview logic
from .interview_views import (
    interviews_list,
    add_interview,
    interview_details,
    edit_interview,
    delete_interview,
)
from .dashboard_views import dashboard

# candidate logic 
from .candidate_views import (
    candidates_list,
    candidate_details,
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
    job_details,
)
#applications logic
from .application_views import (
    applications_list,
    application_details,
   
)
# interview logic
from .interview_views import (
    interviews_list,
    add_interview,
    interview_details,
    edit_interview,
    delete_interview,
)
#evaluation logic
from .evaluation_views import (
    evaluations_list,
    add_evaluation,
    evaluation_details,
    edit_evaluation,
    delete_evaluation,
)
#activity logic
from .activity_views import (
    activities_list,
    add_activity,
    activity_details,
    edit_activity,
    delete_activity,
)
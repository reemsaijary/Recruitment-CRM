from django.contrib import admin

from .models import Company
from .models import Candidate
from .models import Job
from .models import Application
from .models import Interview
from .models import Evaluation


# Register models in Django admin panel

admin.site.register(Company)
admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Interview)
admin.site.register(Evaluation)
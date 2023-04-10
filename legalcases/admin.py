from django.contrib import admin
from .models import Cases, CaseComments, CasePresentations
# Register your models here.

admin.site.register(Cases)
admin.site.register(CaseComments)
admin.site.register(CasePresentations)
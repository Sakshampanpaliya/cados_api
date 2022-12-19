from django.contrib import admin
from .models import Advocate
from .models import Company
# Register your models here.
#For the table view
class AdvocateAdmin(admin.ModelAdmin):
    list_Display=('username','bio','company')

admin.site.register(Advocate,AdvocateAdmin)
admin.site.register(Company)

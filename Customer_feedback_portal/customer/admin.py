from django.contrib import admin
from customer.models import feedback

class FeedbackAdmin(admin.ModelAdmin):
    fields = ['Name','Customer_id','Mobile_Number','Gender','Address','feedback']

admin.site.register(feedback,FeedbackAdmin)

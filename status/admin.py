from django.contrib import admin

from .models import Status
from .forms import StatusForm

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']  # __str__ instead of content
    form = StatusForm
    # class Meta:
    #     model = Status

admin.site.register(Status, StatusAdmin)
from django.contrib import admin
from .models import HistoryModel, TagModel, CustomUserModel

# Register your models here.
admin.site.register(HistoryModel)
admin.site.register(TagModel)
admin.site.register(CustomUserModel)

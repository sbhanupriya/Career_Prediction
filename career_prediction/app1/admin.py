from django.contrib import admin
from .models import dataset
from .models import page
# Register your models here.
admin.site.register(dataset)
admin.site.register(page)
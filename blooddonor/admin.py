# blooddonor/admin.py

from django.contrib import admin
from .models import Donor  # Import your models

admin.site.register(Donor)  # Register your models


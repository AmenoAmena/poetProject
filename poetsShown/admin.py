from django.contrib import admin
from .models import poets_shown,poet_author

# Register your models here.
admin.site.register(poets_shown)
admin.site.register(poet_author)
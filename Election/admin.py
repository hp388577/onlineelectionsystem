from django.contrib import admin

# Register your models here.
from .models import Election,Area,Vote
# Register your models here.
admin.site.register(Area)
admin.site.register(Election)
admin.site.register(Vote)
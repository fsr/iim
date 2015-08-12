from django.contrib import admin
import reversion

# Register your models here.
from .models import Info 

@admin.register(Info)
class InfoAdmin(reversion.VersionAdmin):
    list_display = ('priority', 'subject', 'created')
    list_display_links = list_display
    search_fields = ('subject', 'details')
    list_filter = ('priority', 'created')

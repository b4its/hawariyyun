from django.contrib import admin
from .models import kritik_saran
from django.conf import settings
# Register your models here.
@admin.register(kritik_saran)
class kritik_saranAdmin(admin.ModelAdmin):
 list_display = ('user','jenis','pembahasan','status')

from django.contrib import admin
from .models import *
# Register your models here.

class UploadBerkasAdmin(admin.ModelAdmin):
    readonly_fields = [
        'uploaded',
        'slug'
    ]

class RekapBerkasAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug'
    ]

admin.site.register(UploadBerkasJurnal, UploadBerkasAdmin)
admin.site.register(UploadBerkasProsiding, UploadBerkasAdmin)
admin.site.register(UploadBerkasBuku, UploadBerkasAdmin)
admin.site.register(UploadBerkasHaki, UploadBerkasAdmin)
admin.site.register(Reviewer)
admin.site.register(Admin)
admin.site.register(PenilaianBerkasJurnal, RekapBerkasAdmin)
admin.site.register(PenilaianBerkasProsiding, RekapBerkasAdmin)
admin.site.register(PenilaianBerkasBuku, RekapBerkasAdmin)
admin.site.register(PenilaianBerkasHaki, RekapBerkasAdmin)
admin.site.register(PlagiasiLinieritas, RekapBerkasAdmin)
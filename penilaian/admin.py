from django.contrib import admin
from .models import *
# Register your models here.

class UploadBerkasAdmin(admin.ModelAdmin):
    readonly_fields = [
        'uploaded',
        'slug',
    ]

class PenilaianBerkasAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
        'slug'
    ]

admin.site.register(UploadBerkasJurnal, UploadBerkasAdmin)
admin.site.register(UploadBerkasProsiding, UploadBerkasAdmin)
admin.site.register(UploadBerkasBuku, UploadBerkasAdmin)
admin.site.register(UploadBerkasHaki, UploadBerkasAdmin)
admin.site.register(Reviewer)
admin.site.register(Admin)
admin.site.register(Users)
admin.site.register(PenulisLain)
admin.site.register(PenilaianBerkasJurnal, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasProsiding, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasBuku, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasHaki, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasJurnal2, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasProsiding2, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasBuku2, PenilaianBerkasAdmin)
admin.site.register(PenilaianBerkasHaki2, PenilaianBerkasAdmin)